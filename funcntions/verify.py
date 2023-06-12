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

def placa_existe(placa):
    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()

    comando = "SELECT COUNT(*) FROM veiculo WHERE placa = ?"
    cursor.execute(comando, (placa,))
    resultado = cursor.fetchone()[0]

    conn.close()

    return resultado > 0

def cpf_existe(cpf_dono):

    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()

    comando = "SELECT COUNT(*) FROM Usuario WHERE CPF = ?"
    cursor.execute(comando, (cpf_dono,))
    resultado = cursor.fetchone()[0]

    conn.close()

    return resultado < 1

def cpf_existe_nao(cpf_dono):

    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()

    comando = "SELECT COUNT(*) FROM Usuario WHERE CPF = ?"
    cursor.execute(comando, (cpf_dono,))
    resultado = cursor.fetchone()[0]

    conn.close()

    return resultado > 0 