import sqlite3
from helped_function import utworz_tabele, wyswietl_liste_studentow, znajdz_id, wyczysc_tabele

#Funkcje CRUD
def dodaj_studenta(imie, nazwisko):
    if not (isinstance(imie, str) and isinstance(nazwisko, str)): return 1
    if(imie == "" or nazwisko == "" ): return 0
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO listaStudentow (Imie, Nazwisko) VALUES (?, ?)", (imie, nazwisko))
    conn.commit()
    conn.close()
    print("Student został dodany do bazy danych.")

def wyswietl_dane_studenta(student_id):
    if not isinstance(student_id, int): return 0
    if student_id < 1: return 1
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Imie, Nazwisko FROM listaStudentow WHERE ID=?", (student_id,))
    student = cursor.fetchone()
    conn.close()

    if not student:
        return None 
    else:
        student_data = {
            "ID": student_id,
            "Imie": student[0],
            "Nazwisko": student[1]
        }
        return student_data  


def aktualizuj_dane_studenta(student_id, imie, nazwisko):
    if not (isinstance(student_id, int) or student_id is None): return 0
    if not (isinstance(imie, str) or student_id is None): return 1
    if not (isinstance(nazwisko, str) or student_id is None): return 2
    tmp = wyswietl_dane_studenta(student_id)
    if tmp is None:
        print("Brak studenta w bazie danych")
        return 4
    
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE listaStudentow SET Imie=?, Nazwisko=? WHERE ID=?", (imie, nazwisko, student_id))
    conn.commit()
    conn.close()
    print("Dane studenta zostały zaktualizowane.")

def usun_studenta(student_id):
    if not isinstance(student_id, int): return 0
    tmp = wyswietl_dane_studenta(student_id)
    if tmp is None:
        print("Brak studenta w bazie danych")
        return 1
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM listaStudentow WHERE ID=?", (student_id,))
    conn.commit()
    conn.close()
    print("Student został usunięty z bazy danych.")
