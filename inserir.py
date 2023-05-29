import sqlite3

conn = sqlite3.connect('exemplo.db')

cursor = conn.cursor()

inserir_dados = '''INSERT INTO prokemon VALUES (4,'KRUGE','AGUA');

'''
cursor.execute(inserir_dados)

conn.commit()
conn.close()