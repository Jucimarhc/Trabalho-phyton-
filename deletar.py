import sqlite3
from tkinter import messagebox

def excluir_dado(usuario_del):

    # Conexão com o banco de dados
    conn = sqlite3.connect('Banco_PY.db')
    cursor = conn.cursor()

    # Capturar o dado a ser excluído
    dado_para_excluir = usuario_del.get()

    # Executar o comando de exclusão na tabela funcionario
    cursor.execute("DELETE FROM Funcionario WHERE login=?", (dado_para_excluir,))
    messagebox.showinfo("Sucesso", "Usuario deletado!")

    # Salvar as alterações e fechar a conexão com o banco
    conn.commit()
    conn.close()
