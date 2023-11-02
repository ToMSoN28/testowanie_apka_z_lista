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


def aktualizuj_dane_studenta():
    student_id = int(input("Podaj ID studenta, którego dane chcesz zaktualizować: "))
    imie = input("Nowe imię studenta: ")
    nazwisko = input("Nowe nazwisko studenta: ")

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
        return
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM listaStudentow WHERE ID=?", (student_id,))
    conn.commit()
    conn.close()
    print("Student został usunięty z bazy danych.")

    # if not student_id:
    #     return print("Nie istnieje")
    # else:
    #     return student_id[0]
    

#Program
if __name__ == "__main__":
    utworz_tabele()

    while True:
        print("\nWybierz operację:")
        print("1. Dodaj studenta")
        print("2. Wyświetl studenta")
        print("3. Aktualizuj dane studenta")
        print("4. Usuń studenta")
        print("5. Wyświetl listę studentów")
        print("6. Znajdź ID na podstawie nazwiska")
        print("0. Wyjście")

        wybor = input("Twój wybór: ")

        if wybor == "1":
            imie = input("Podaj imię studenta: ")
            nazwisko = input("Podaj nazwisko studenta: ")
            dodaj_studenta(imie, nazwisko)

        elif wybor == "2":
            student_id = int(input("Podaj ID studenta, którego dane chcesz wyświetlić: "))
            student_data = wyswietl_dane_studenta(student_id)
            if student_data:
                print(f"ID: {student_data['ID']}, Imię: {student_data['Imie']}, Nazwisko: {student_data['Nazwisko']}")
            else:
                print("Brak studenta w bazie danych.")


        elif wybor == "3":
            aktualizuj_dane_studenta()

        elif wybor == "4":
            student_id = int(input("Podaj ID studenta, którego chcesz usunąć: "))
            usun_studenta(student_id)

        elif wybor == "5":
            students = wyswietl_liste_studentow()
            if students is not None:
                for student in students:
                    print(f"ID: {student[0]}, Imię: {student[1]}, Nazwisko: {student[2]}")
            else:
                print("Brak studentów w bazie danych.")

        elif wybor == "6":
            nazwisko = input("Podaj nazwisko studenta: ")
            student_id = znajdz_id(nazwisko)
            if student_id is not None:
                print(f"ID studenta: {student_id}")
            else:
                print(f"Brak studenta o nazwisku {nazwisko} w bazie danych.")

        elif wybor == "0":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór.")
