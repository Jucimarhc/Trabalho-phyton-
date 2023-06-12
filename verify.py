import sqlite3

def login_existe(login):
    conn = sqlite3.connect("Banco_PY.db")
    cursor = conn.cursor()

    comando = "SELECT COUNT(*) FROM Funcionario WHERE login = ?"
    cursor.execute(comando, (login,))
    resultado = cursor.fetchone()[0]

    conn.close()

    return resultado > 0

def placa_existe(placa):
    conn = sqlite3.connect("Banco_PY.db")
    cursor = conn.cursor()

    comando = "SELECT COUNT(*) FROM veiculo WHERE placa = ?"
    cursor.execute(comando, (placa,))
    resultado = cursor.fetchone()[0]

    conn.close()

    return resultado > 0