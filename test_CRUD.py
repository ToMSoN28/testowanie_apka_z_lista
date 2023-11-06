import sqlite3
import unittest
from main import dodaj_studenta, wyswietl_dane_studenta, usun_studenta, aktualizuj_dane_studenta
from helped_function import utworz_tabele, wyswietl_liste_studentow, znajdz_id, znajdz_najwyzsze_id


class TestDatabaseCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect('listaStudentow.db')

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def setUp(self):
        utworz_tabele()

    def test_dodaj_studenta(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        cursor = self.conn.cursor()
        cursor.execute("SELECT Imie, Nazwisko FROM listaStudentow WHERE Imie=? AND Nazwisko=?", (imie, nazwisko))
        student = cursor.fetchone()
        self.assertIsNotNone(student)
        student_id = znajdz_id(nazwisko)
        self.conn.commit()
        cursor.close()
        usun_studenta(student_id)
        
    def test_dodaj_studenta_puste_imie(self):
        imie = ""
        nazwisko = "Zukowski"
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_puste_nazwisko(self):
        imie = "Jan"
        nazwisko = ""
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_puste_imie_i_nazwisko(self):
        imie = ""
        nazwisko = ""
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_None_imie(self):
        imie = None
        nazwisko = "Zukowski"
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_None_nazwisko(self):
        imie = "Jan"
        nazwisko = None
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_None_imie_i_nazwisko(self):
        imie = None
        nazwisko = None
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_not_string_imie(self):
        imie = 123
        nazwisko = "Zukowski"
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_not_string_nazwisko(self):
        imie = "Jan"
        nazwisko = 123
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_not_string_imie_i_nazwisko(self):
        imie = 123
        nazwisko = 123
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_wyswietl_dane_studenta_istnieje(self):
        imie = "Anna"
        nazwisko = "Nowak"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        student_data = wyswietl_dane_studenta(student_id)
        self.assertIsNotNone(student_data)
        self.assertEqual(student_data["Imie"], imie)
        self.assertEqual(student_data["Nazwisko"], nazwisko)
        usun_studenta(student_id)

    
    def test_wyswietl_dane_studenta_nie_istnieje(self):
        student_id = 112333455
        student_data = wyswietl_dane_studenta(student_id)
        self.assertIsNone(student_data) 
        
    def test_wyswietl_dane_studenta_id_ujemne(self):
        student_id = -1
        student_data = wyswietl_dane_studenta(student_id)
        self.assertEqual(1, student_data)
        
    def test_wyswietl_dane_studenta_id_zero(self):
        student_id = 0
        student_data = wyswietl_dane_studenta(student_id)
        self.assertEqual(1, student_data)
        
    def test_wyswietl_dane_studenta_id_nie_int(self):
        student_id = "123"
        student_data = wyswietl_dane_studenta(student_id)
        self.assertEqual(0, student_data) 
        
    def test_wyswietl_dane_studenta_id_None(self):
        student_id = None
        student_data = wyswietl_dane_studenta(student_id)
        self.assertEqual(0, student_data) 
        
    def test_aktualizuj_dane_studenta_imie(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        imie = "John"
        aktualizuj_dane_studenta(student_id, imie, nazwisko)
        cursor = self.conn.cursor()
        cursor.execute("SELECT Imie, Nazwisko FROM listaStudentow WHERE Imie=? AND Nazwisko=?", (imie, nazwisko))
        student = cursor.fetchone()
        self.assertIsNotNone(student)
        student_id = znajdz_id(nazwisko)
        self.conn.commit()
        cursor.close()
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_nazwisko(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        nazwisko = "Smith"
        aktualizuj_dane_studenta(student_id, imie, nazwisko)
        cursor = self.conn.cursor()
        cursor.execute("SELECT Imie, Nazwisko FROM listaStudentow WHERE Imie=? AND Nazwisko=?", (imie, nazwisko))
        student = cursor.fetchone()
        self.assertIsNotNone(student)
        student_id = znajdz_id(nazwisko)
        self.conn.commit()
        cursor.close()
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_imie_nazwisko(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        imie = "John"
        nazwisko = "Smith"
        aktualizuj_dane_studenta(student_id, imie, nazwisko)
        cursor = self.conn.cursor()
        cursor.execute("SELECT Imie, Nazwisko FROM listaStudentow WHERE Imie=? AND Nazwisko=?", (imie, nazwisko))
        student = cursor.fetchone()
        self.assertIsNotNone(student)
        student_id = znajdz_id(nazwisko)
        self.conn.commit()
        cursor.close()
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_id_not_int(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = "test"
        self.assertEqual(0, aktualizuj_dane_studenta(student_id, imie, nazwisko))
        student_id = znajdz_id(nazwisko)
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_imie_not_string(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        imie = 2137
        self.assertEqual(1, aktualizuj_dane_studenta(student_id, imie, nazwisko))
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_nazwisko_not_string(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        nazwisko = 8
        self.assertEqual(1, aktualizuj_dane_studenta(student_id, imie, nazwisko))
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_brak_studenta(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_najwyzsze_id() + 1
        self.assertEqual(2, aktualizuj_dane_studenta(student_id, imie, nazwisko))
        student_id = znajdz_id(nazwisko)
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_puste_imie(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        imie = ""
        self.assertEqual(3, aktualizuj_dane_studenta(student_id, imie, nazwisko))
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_puste_nazwisko(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        nazwisko = ""
        self.assertEqual(3, aktualizuj_dane_studenta(student_id, imie, nazwisko))
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_id_None(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = None
        self.assertEqual(0, aktualizuj_dane_studenta(student_id, imie, nazwisko))
        student_id = znajdz_id(nazwisko)
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_id_ujemne(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = -1
        self.assertEqual(0, aktualizuj_dane_studenta(student_id, imie, nazwisko))
        student_id = znajdz_id(nazwisko)
        usun_studenta(student_id)

    def test_aktualizuj_dane_studenta_id_not_int(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = "123"
        self.assertEqual(0, aktualizuj_dane_studenta(student_id, imie, nazwisko))
        student_id = znajdz_id(nazwisko)
        usun_studenta(student_id)
        
    def test_usun_studenta(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        usun_studenta(student_id)
        cursor = self.conn.cursor()
        cursor.execute("SELECT ID FROM listaStudentow WHERE ID=?", (student_id,))
        student = cursor.fetchone()
        cursor.close()
        self.assertIsNone(student)

    def test_usun_studenta_id_not_int(self):
        student_id = "123"
        self.assertEqual(0, usun_studenta(student_id))

    def test_usun_studenta_id_None(self):
        student_id = None
        self.assertEqual(0, usun_studenta(student_id))

    def test_usun_studenta_id_ujemne(self):
        student_id = -1
        self.assertEqual(2, usun_studenta(student_id))


    def test_usun_studenta_brak_studenta(self):
        imie = "Jan"
        nazwisko = "Zukowski"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_najwyzsze_id() + 1
        self.assertEqual(1, usun_studenta(student_id))
        student_id = znajdz_id(nazwisko)
        usun_studenta(student_id)


if __name__ == "__main__":
    unittest.main()
