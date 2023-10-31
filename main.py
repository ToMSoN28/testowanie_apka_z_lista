import sqlite3

def utworz_tabele():
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS listaStudentow (
                      ID INTEGER PRIMARY KEY,
                      Imie TEXT,
                      Nazwisko TEXT
                  )''')
    conn.commit()
    conn.close()

def dodaj_studenta():
    imie = input("Podaj imię studenta: ")
    nazwisko = input("Podaj nazwisko studenta: ")

    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO listaStudentow (Imie, Nazwisko) VALUES (?, ?)", (imie, nazwisko))
    conn.commit()
    conn.close()
    print("Student został dodany do bazy danych.")

def wyswietl_liste_studentow():
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Imie, Nazwisko FROM listaStudentow")
    students = cursor.fetchall()
    conn.close()

    if not students:
        print("Brak studentów w bazie danych.")
    else:
        for student in students:
            print(f"ID: {student[0]}, Imię: {student[1]}, Nazwisko: {student[2]}")
            
def wyswietl_dane_studenta():
    student_id = int(input("Podaj ID studenta, którego dane chcesz wyświetlić: "))
    
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Imie, Nazwisko FROM listaStudentow WHERE ID=?", (student_id,))
    student = cursor.fetchone()
    conn.close()

    if not student:
        print("Brak studenta w bazie danych.")
    else:
        print(f"ID: {student_id}, Imię: {student[0]}, Nazwisko: {student[1]}")


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

def usun_studenta():
    student_id = int(input("Podaj ID studenta, którego chcesz usunąć: "))

    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM listaStudentow WHERE ID=?", (student_id,))
    conn.commit()
    conn.close()
    print("Student został usunięty z bazy danych.")

if __name__ == "__main__":
    utworz_tabele()

    while True:
        print("\nWybierz operację:")
        print("1. Dodaj studenta")
        print("2. Wyświetl studenta")
        print("3. Aktualizuj dane studenta")
        print("4. Usuń studenta")
        print("5. Wyświetl listę studentów")
        print("0. Wyjście")

        wybor = input("Twój wybór: ")

        if wybor == "1":
            dodaj_studenta()
        elif wybor == "2":
            wyswietl_dane_studenta()
        elif wybor == "3":
            aktualizuj_dane_studenta()
        elif wybor == "4":
            usun_studenta()
        elif wybor == "5":
            wyswietl_liste_studentow()
        elif wybor == "0":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór.")
