import sqlite3

conn = sqlite3.connect('exemplo.db')

cursor = conn.cursor()

visualizar_dados = '''SELECT * FROM prokemon;
'''
cursor.execute(visualizar_dados)

for linha in cursor.fetchall():
    print(linha)

conn.commit()
conn.close()