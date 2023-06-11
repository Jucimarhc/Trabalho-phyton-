import sqlite3

def login_existe(login):
    conn = sqlite3.connect("Banco_PY.db")
    cursor = conn.cursor()

    comando = "SELECT COUNT(*) FROM Funcionario WHERE login = ?"
    cursor.execute(comando, (login,))
    resultado = cursor.fetchone()[0]

    conn.close()

    return resultado > 0