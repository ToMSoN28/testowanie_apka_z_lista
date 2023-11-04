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
    
def wyswietl_liste_studentow():
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Imie, Nazwisko FROM listaStudentow")
    students = cursor.fetchall()
    conn.close()
    if not students:
        return None
    else:
        return students 
    
def znajdz_id(nazwisko):
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ID FROM listaStudentow WHERE Nazwisko=?", (nazwisko,))
    student_id = cursor.fetchone()
    conn.close()

    if not student_id:
        return print("Nie istnieje")
    else:
        return student_id[0]
    
def wyczysc_tabele():
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM listaStudentow')
    conn.commit()
    conn.close()
def znajdz_najwyzsze_id():
    conn = sqlite3.connect('listaStudentow.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ID FROM listaStudentow ORDER BY ID DESC LIMIT 1")
    ostatni_student = cursor.fetchone()
    if ostatni_student:
        conn.commit()
        conn.close()
        return ostatni_student[0]
    else:
        conn.commit()
        conn.close()
        return None
