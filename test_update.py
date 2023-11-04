import sqlite3
import unittest

from helped_function import znajdz_najwyzsze_id
from main import utworz_tabele, dodaj_studenta, usun_studenta, znajdz_id, \
    aktualizuj_dane_studenta


class TestDatabaseCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect('listaStudentow.db')

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def setUp(self):
        utworz_tabele()

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


if __name__ == "__main__":
    unittest.main()