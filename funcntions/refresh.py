import tkinter as tk

import sqlite3
caminho_bd = r'banco\Banco_PY.db'
conn = sqlite3.connect(caminho_bd)

import sys
sys.path.append('funcntions')

#----------------------------Froms---------------------------------------------------#
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, font
from tkinter import ttk

def atualizar_treeview(tree):
    # Limpar todos os itens do treeview
    tree.delete(*tree.get_children())

    # Consultar os registros do banco de dados
    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM veiculo")
    registros = cursor.fetchall()
    conn.close()

    # Atualizar o treeview com os novos registros
    for registro in registros:
        tree.insert("", "end", values=registro)

