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

    def test_wyswietl_dane_studenta_instnieje(self):
        imie = "Anna"
        nazwisko = "Nowak"
        dodaj_studenta(imie, nazwisko)
        student_id = znajdz_id(nazwisko)
        student_data = wyswietl_dane_studenta(student_id)
        self.assertIsNotNone(student_data)
        self.assertEqual(student_data["Imie"], imie)
        self.assertEqual(student_data["Nazwisko"], nazwisko)
        usun_studenta(student_id)

    
    def test_wyswietl_dane_studenta_nie_instnieje(self):
        student_id = 112333455
        student_data = wyswietl_dane_studenta(student_id)
        self.assertIsNone(student_data) 
        
    def test_wyswietl_dane_studenta_id_nie_int(self):
        student_id = "123"
        student_data = wyswietl_dane_studenta(student_id)
        self.assertEqual(0, student_data) 
        
    def test_wyswietl_dane_studenta_id_None(self):
        student_id = None
        student_data = wyswietl_dane_studenta(student_id)
        self.assertEqual(0, student_data) 
        

if __name__ == "__main__":
    unittest.main()
        