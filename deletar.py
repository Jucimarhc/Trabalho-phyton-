import sqlite3

conn = sqlite3.connect('exemplo.db')

cursor = conn.cursor()

deletar_dados = '''DELETE FROM prokemon WHERE id = 3;

'''
cursor.execute(deletar_dados)

conn.commit()
conn.close()