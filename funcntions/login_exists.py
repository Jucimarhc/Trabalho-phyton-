import sqlite3
caminho_bd = r'banco\Banco_PY.db'
conn = sqlite3.connect(caminho_bd)

def login_existe(login):
    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()

    comando = "SELECT COUNT(*) FROM Funcionario WHERE login = ?"
    cursor.execute(comando, (login,))
    resultado = cursor.fetchone()[0]

    conn.close()

    return resultado > 0
