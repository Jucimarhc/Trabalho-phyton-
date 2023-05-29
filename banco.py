import sqlite3

conn = sqlite3.connect('exemplo.db')

cursor = conn.cursor()

criar_tabela_pessoa = '''CREATE TABLE prokemon(
  id INTEGER NOT NULL,
  nome VARCHAR(30),
  tipo VARCHAR(15),
  PRIMARY KEY(id)
);

'''
cursor.execute(criar_tabela_pessoa)
conn.commit()
conn.close()