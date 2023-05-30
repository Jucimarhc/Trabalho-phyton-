import sqlite3

def abrir_banco():

  conn = sqlite3.connect("Banco_PY.db")
  cursor = conn.cursor()
  try:
    comando = ''' SELECT * FROM Funcionario
'''
    cursor.execute(comando)
    for linha in cursor.fetchall():
      print(linha)
  except TypeError as erro:
    print(erro)
  
  conn.commit()
  conn.close()