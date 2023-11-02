from main import dodaj_studenta, wyswietl_dane_studenta, aktualizuj_dane_studenta, usun_studenta
from helped_function import utworz_tabele, wyswietl_liste_studentow, znajdz_id, wyczysc_tabele

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
        print("7. Wyczyść liste")
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
            student_id = int(input("Podaj ID studenta, którego dane chcesz zaktualizować: "))
            imie = input("Nowe imię studenta: ")
            nazwisko = input("Nowe nazwisko studenta: ")
            aktualizuj_dane_studenta(student_id, imie, nazwisko)

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
        
        elif wybor == "7":
            wyczysc_tabele()
            print("Lista została wyczyszczona")
        
        elif wybor == "0":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór.")
