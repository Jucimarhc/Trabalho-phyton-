import sqlite3
import threading

# Cria um objeto de bloqueio
lock = threading.Lock()

def inserir_dado(login, senha, nome):
    print("Rodou e acrescentou algo útil")

    with lock:  # Adquire o bloqueio
        conn = sqlite3.connect('Banco_PY.db')
        cursor = conn.cursor()

        inserir_dados = '''INSERT INTO Funcionario (login, nome, senha) VALUES (?, ?, ?);'''
        dados = (login, nome, senha)
        
        cursor.execute(inserir_dados, dados)

        conn.commit()
        conn.close()
        # O bloqueio é liberado automaticamente quando o contexto é encerrado
