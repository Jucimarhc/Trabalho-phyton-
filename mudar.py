import sqlite3
def mudar_dado():
    
    print("rodoufo mudou")
    conn = sqlite3.connect('Banco_PY.db')

    cursor = conn.cursor()

    inserir_dados = '''UPDATE Usuario
    SET Nome = 'Marrocos'
    WHERE CPF = '32323232332';
    '''
    cursor.execute(inserir_dados)

    conn.commit()
    conn.close()