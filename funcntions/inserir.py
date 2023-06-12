import sqlite3
caminho_bd = r'banco\Banco_PY.db'
conn = sqlite3.connect(caminho_bd)

import threading

# Cria um objeto de bloqueio
lock = threading.Lock()

def inserir_dado(login, senha, nome):
    print("Rodou e acrescentou algo útil")

    with lock:  # Adquire o bloqueio
        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()

        inserir_dados = '''INSERT INTO Funcionario (login, nome, senha) VALUES (?, ?, ?);'''
        dados = (login, nome, senha)

        cursor.execute(inserir_dados, dados)

        conn.commit()
        conn.close()
        # O bloqueio é liberado automaticamente quando o contexto é encerrado

def inserir_veiculo(placa,modelo,entrada,saida,dono):

    with lock:  # Adquire o bloqueio
        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()

        inserir_dados_veiculo = '''INSERT INTO veiculo (Placa, Modelo, Hora_chegada, Hora_saida, Dono_CPF) VALUES (?, ?, ?, ?, ?);'''
        dados_veiculo = (placa,modelo,entrada,saida,dono)

        cursor.execute(inserir_dados_veiculo, dados_veiculo)

        conn.commit()
        conn.close()