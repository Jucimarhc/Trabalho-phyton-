import sqlite3
caminho_bd = r'banco\Banco_PY.db'
conn = sqlite3.connect(caminho_bd)

from tkinter import messagebox

def excluir_dado(usuario_del):

    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()

    dado_para_excluir = usuario_del.get()

    cursor.execute("DELETE FROM Funcionario WHERE login=?", (dado_para_excluir,))
    messagebox.showinfo("Sucesso", "Usuario deletado!")

    conn.commit()
    conn.close()
