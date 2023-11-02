import sqlite3
import unittest
from main import dodaj_studenta, wyswietl_dane_studenta, usun_studenta
from helped_function import utworz_tabele, wyswietl_liste_studentow, znajdz_id

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
        usun_studenta(student_id)
        

    def test_dodaj_studenta_puste_imie(self):
        imie = ""
        nazwisko = "Zukowski"
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        # cursor = self.conn.cursor()
        # cursor.execute("SELECT Imie, Nazwisko FROM listaStudentow WHERE Imie=? AND Nazwisko=?", (imie, nazwisko))
        # student = cursor.fetchone()
        # self.assertIsNone(student)


        
    def test_dodaj_studenta_puste_nazwisko(self):
        imie = "Jan"
        nazwisko = ""
        self.assertEqual(0, dodaj_studenta(imie, nazwisko))
        # cursor = self.conn.cursor()
        # cursor.execute("SELECT Imie, Nazwisko FROM listaStudentow WHERE Imie=? AND Nazwisko=?", (imie, nazwisko))
        # student = cursor.fetchone()
        # self.assertIsNone(student)
        
    def test_dodaj_studenta_None_imie(self):
        imie = None
        nazwisko = "Zukowski"
        self.assertEqual(1, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_None_nazwisko(self):
        imie = "Jan"
        nazwisko = None
        self.assertEqual(1, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_not_string_imie(self):
        imie = 123
        nazwisko = "Zukowski"
        self.assertEqual(1, dodaj_studenta(imie, nazwisko))
        
    def test_dodaj_studenta_not_string_nazwisko(self):
        imie = "Jan"
        nazwisko = 123
        self.assertEqual(1, dodaj_studenta(imie, nazwisko))
        

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
        


    # def test_wyswietl_liste_studentow(self):
    #     students = wyswietl_liste_studentow()
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT COUNT(*) FROM listaStudentow")
    #     expected = cursor.fetchone()[0] 
    #     print(expected)
    #     actual = len(students)
    #     self.assertEqual(expected, actual)

  


if __name__ == "__main__":
    unittest.main()
        