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

    tree.delete(*tree.get_children())

    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM veiculo")
    registros = cursor.fetchall()
    conn.close()

    for registro in registros:
        tree.insert("", "end", values=registro)

def pesquisa_dados(entry, tree):
   
    valor_busca = entry.get() 
    
    tree.delete(*tree.get_children())
    
    if not valor_busca:

        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()
    
        cursor.execute("SELECT veiculo.Placa, veiculo.Modelo, veiculo.Hora_chegada, veiculo.Hora_saida, Usuario.Nome FROM veiculo JOIN Usuario ON veiculo.Dono_CPF = Usuario.CPF")
    
        resultados = cursor.fetchall()
    
        for resultado in resultados:
            tree.insert('', 'end', values=resultado)

        cursor.close()
        conn.close()

        return

    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(veiculo)")
    colunas = [coluna[1] for coluna in cursor.fetchall()]
    
    consulta = "SELECT veiculo.Placa, veiculo.Modelo, veiculo.Hora_chegada, veiculo.Hora_saida, Usuario.Nome FROM veiculo JOIN Usuario ON veiculo.Dono_CPF = Usuario.CPF WHERE "
    condicoes = []
    for coluna in colunas:
        condicoes.append(f"{coluna} = ?")
    consulta += " OR ".join(condicoes)
    
    cursor.execute(consulta, tuple([valor_busca] * len(colunas)))

    resultados = cursor.fetchall()

    for resultado in resultados:
        tree.insert('', 'end', values=resultado)

    cursor.close()
    conn.close()


