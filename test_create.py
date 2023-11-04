import sqlite3
import unittest
import main
from main import utworz_tabele, dodaj_studenta, wyswietl_dane_studenta, usun_studenta, znajdz_id, wyswietl_liste_studentow

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
        self.assertEqual(1, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_puste_nazwisko(self):
        imie = "Jan"
        nazwisko = ""
        self.assertEqual(1, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_None_imie(self):
        imie = None
        nazwisko = "Zukowski"
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_None_nazwisko(self):
        imie = "Jan"
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
        
if __name__ == "__main__":
    unittest.main()
        