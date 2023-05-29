import sqlite3

conn = sqlite3.connect('exemplo.db')

cursor = conn.cursor()

inserir_dados = '''UPDATE prokemon
SET nome = 'PIKACHOLAS'
WHERE id = 1;
'''
cursor.execute(inserir_dados)

conn.commit()
conn.close()