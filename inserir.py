import sqlite3
def inserir_dado():
    
    print("rodoufo acrescentou algo util")
    conn = sqlite3.connect('Banco_PY.db')

    cursor = conn.cursor()

    inserir_dados = '''INSERT INTO Funcionario VALUES ('1','ADMIN','ADMIN','Ateb@2022');

    '''
    cursor.execute(inserir_dados)

    conn.commit()
    conn.close()