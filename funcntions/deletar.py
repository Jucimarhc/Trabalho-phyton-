import sqlite3
caminho_bd = r'banco\Banco_PY.db'
conn = sqlite3.connect(caminho_bd)

from tkinter import messagebox

def excluir_dado(usuario_del):

    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()

    dado_para_excluir = usuario_del.get()

    cursor.execute("DELETE FROM Funcionario WHERE login=?", (dado_para_excluir,))
    messagebox.showinfo("Sucesso", "Login deletado!")

    conn.commit()
    conn.close()


def excluir_user(deletar_cpf):

    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM veiculo WHERE Dono_CPF IN (SELECT CPF FROM Usuario WHERE CPF=?)", (deletar_cpf,))
    cursor.execute("DELETE FROM Usuario WHERE CPF=?", (deletar_cpf,))
    messagebox.showinfo("Sucesso", "Usuario deletado!")

    conn.commit()
    conn.close()
