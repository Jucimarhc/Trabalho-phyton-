import sqlite3  
def ver_dado():
    
    print("rodoufo viu")

    conn = sqlite3.connect('Banco_PY.db')

    cursor = conn.cursor()

    visualizar_dados = '''SELECT * FROM Usuario;
    '''
    cursor.execute(visualizar_dados)

    for linha in cursor.fetchall():
        print(linha)

    conn.commit()
    conn.close()