import sqlite3
def deletar_dado():
    
    print("rodoufo faliu e morreu")
    conn = sqlite3.connect('Banco_PY.db')

    cursor = conn.cursor()

   # deletar_dados = '''DELETE FROM prokemon WHERE id = 3;

  #  '''
  #  cursor.execute()

    conn.commit()
    conn.close()