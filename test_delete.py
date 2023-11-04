import sqlite3
import unittest

from helped_function import znajdz_najwyzsze_id
from main import utworz_tabele, dodaj_studenta, usun_studenta, znajdz_id

class TestDatabaseCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect('listaStudentow.db')

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def setUp(self):
        utworz_tabele()

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

