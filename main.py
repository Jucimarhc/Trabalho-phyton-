#--------------------------Imports---------------------------------------------------#
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
#----------------------------Funções-------------------------------------------------#
from verify import login_existe, placa_existe
from inserir import inserir_dado, inserir_veiculo
from deletar import excluir_dado

def verificar_login():
    
    login = entrada_usuario.get()
    senha = entrada_senha.get()

    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()

    cursor.execute("SELECT Senha FROM Funcionario WHERE Login=?", (login,))
    resultado = cursor.fetchone()
    
    if resultado:
        #Aqui ele pega o resultado do banco e manda pras 3 variaveis
        senha_funcionario = resultado[0]
        if senha == senha_funcionario:
            messagebox.showinfo("SUCESSO", "Login bem-sucedido!")
            tela_login.withdraw()
            tela.deiconify()
        else:
            messagebox.showerror("ERRO", "Senha incorreta!")
            entrada_senha.delete(0, tk.END)
            entrada_senha.focus()

    else:
        messagebox.showerror("ERRO", "Usuário não encontrado!")
        entrada_usuario.delete(0, tk.END)
        entrada_senha.delete(0, tk.END)
        entrada_usuario.focus()

    conn.commit()
    conn.close()

def login():
    global tela_login, usuario_verify, senha_verify, entrada_usuario, entrada_senha, botao1, usuario, senha, fechar

    def fechar():
        tela_login.destroy()
        sys.exit()

    def pressionar_enter(event):
        botao1.invoke()

    tela_login = tk.Toplevel(tela)
    tela_login.title("Login")
    tela_login.geometry("400x300+500+200")
    tela_login.resizable(False, False)

    usuario_verify = tk.StringVar()
    senha_verify = tk.StringVar()

    custom_font = font.Font(family="Arial", size=12, weight="normal")
    label2 = tk.Label(tela_login, text="Usuário", font=custom_font)
    label2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entrada_usuario = tk.Entry(tela_login, textvariable=usuario_verify)
    entrada_usuario.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    entrada_usuario.focus()
    
    label3 = tk.Label(tela_login, text="Senha", font=custom_font)
    label3.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entrada_senha = tk.Entry(tela_login, textvariable=senha_verify, show='*')
    entrada_senha.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    botao1 = tk.Button(tela_login, text="Login", fg="#FFFFFF", bg="#215470", activebackground="#FFFFFF", width=10, height=1, command=verificar_login)
    botao1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    tela_login.bind('<Return>', pressionar_enter)
    tela_login.protocol("WM_DELETE_WINDOW", fechar)

def criar_tela():
    global tela, tree, adicionar_dado, buscar_tabela_veiculo

    tela = Tk()
    tela.geometry("1280x720")
    tela.configure(bg="#215470")
    tela.title("My Parking Space")
    
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        tela,
        bg="#215470",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    tela.entry_image_1 = entry_image_1  # Armazena a referência como um atributo do objeto tela
    entry_bg_1 = canvas.create_image(491.0, 94.0, image=entry_image_1)

    entry_1 = Entry(
        bd=0,
        bg="#d9d9d9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=136.0,
        y=79.0,
        width=710.0,
        height=28.0
    )

    canvas.create_rectangle(
        121.0,
        144.0,
        901.0,
        694.0,
        fill="#d9d9d9",
        outline=""
    )

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    tela.button_image_1 = button_image_1  # Armazena a referência como um atributo do objeto tela
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=871.0,
        y=79.0,
        width=30.0,
        height=30.0
    )

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    tela.image_image_1 = image_image_1  # Armazena a referência como um atributo do objeto tela
    image_1 = canvas.create_image(1103.0, 143.0, image=image_image_1)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    tela.button_image_2 = button_image_2  # Armazena a referência como um atributo do objeto tela
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (print("button_adicionar clicked"), veiculo_tela()),
        relief="flat"
    )
    button_2.place(
        x=1013.0,
        y=244.0,
        width=180.0,
        height=40.0
    )

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    tela.button_image_3 = button_image_3  # Armazena a referência como um atributo do objeto tela
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_atualizar clicked"),
        relief="flat"
    )
    button_3.place(
        x=1013.0,
        y=320.0,
        width=180.0,
        height=40.0
    )

    tela.resizable(False, False)

    style = ttk.Style()
    style.configure("Custom.Treeview", background="#e1e1e1", foreground="#030303", rowheight=25, borderwidth=2, relief="solid")
    style.configure("Custom.Treeview.Heading", background="#e1e1e1", foreground="#030303", font=("Arial", 12, "bold"))

    tree = ttk.Treeview(tela, style="Custom.Treeview", height=21)

    tree["show"] = "headings"
    tree["columns"] = ("Placa","Modelo", "Entrada","Saída","Dono")

    tree.heading("Placa", text="Placa", anchor=tk.CENTER)
    tree.heading("Modelo", text="Modelo", anchor=tk.CENTER)
    tree.heading("Entrada", text="Entrada", anchor=tk.CENTER)
    tree.heading("Saída", text="Saída", anchor=tk.CENTER)
    tree.heading("Dono", text="Dono", anchor=tk.CENTER)

    tree.column("Placa", minwidth=0, width=140)
    tree.column("Modelo", minwidth=0, width=180)
    tree.column("Entrada", minwidth=0, width=140)
    tree.column("Saída", minwidth=0, width=140)
    tree.column("Dono", minwidth=0, width=179)


    def adicionar_dado():
        tree.delete(*tree.get_children())

    def buscar_tabela_veiculo():

            conn = sqlite3.connect(caminho_bd)
            cursor = conn.cursor()

            cursor.execute("SELECT veiculo.Placa, veiculo.Modelo, veiculo.Hora_chegada, veiculo.Hora_saida, Usuario.Nome FROM veiculo JOIN Usuario ON veiculo.Dono_CPF = Usuario.CPF")

            for linha in cursor.fetchall():
                tree.insert("", tk.END, values=linha)

            cursor.close()
            conn.close()

    buscar_tabela_veiculo()

    tree.grid(row=0, column=0, padx=121, pady=144)

def veiculo_tela():
    global tela_veiculo, entrada_placa_veiculo, entrada_modelo_veiculo, entrada_entrada_veiculo, entrada_saida_veiculo, entrada_dono_veiculo, botao_veiculo1, botao_veiculo2, fechar_veiculo
    
    def fechar_veiculo():
        tela_veiculo.destroy()
    
    tela_veiculo = tk.Toplevel(master=tela)
    tela_veiculo.title("Adicionar Admin")
    tela_veiculo.geometry("400x400+700+200")
    tela_veiculo.resizable(0,0)
    tela_veiculo.transient(tela)

    entrada_placa_veiculo= tk.StringVar()
    entrada_modelo_veiculo = tk.StringVar()
    entrada_entrada_veiculo = tk.StringVar()
    entrada_saida_veiculo = tk.StringVar()
    entrada_dono_veiculo = tk.StringVar()

    label_veiculo1 = tk.Label(tela_veiculo, text="Placa")
    label_veiculo1.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    entrada_placa_veiculo = tk.Entry(tela_veiculo)
    entrada_placa_veiculo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    label_veiculo2 = tk.Label(tela_veiculo, text="Modelo")
    label_veiculo2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entrada_modelo_veiculo = tk.Entry(tela_veiculo)
    entrada_modelo_veiculo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    label_veiculo3 = tk.Label(tela_veiculo, text="Horário de entrada")
    label_veiculo3.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    entrada_entrada_veiculo = tk.Entry(tela_veiculo)
    entrada_entrada_veiculo.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    label_veiculo4 = tk.Label(tela_veiculo, text="Horário de saída")
    label_veiculo4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    entrada_saida_veiculo = tk.Entry(tela_veiculo)
    entrada_saida_veiculo.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    label_veiculo5 = tk.Label(tela_veiculo, text="CPF do dono do Veículo")
    label_veiculo5.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    entrada_dono_veiculo = tk.Entry(tela_veiculo)
    entrada_dono_veiculo.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    botao_veiculo1 = tk.Button(tela_veiculo, text="Salvar", fg="#FFFFFF", width=10, height=1, bg="#215470", activebackground="#FFFFFF", command=botao_veiculo)
    botao_veiculo1.place(relx=0.2, rely=0.8)

    botao_veiculo2 = tk.Button(tela_veiculo, text="Cancelar", fg="#FFFFFF", width=10, height=1, bg="#215470", activebackground="#FFFFFF", command=fechar_veiculo)
    botao_veiculo2.place(relx=0.6, rely=0.8)

def botao_veiculo():
    global criar_placa
    
    criar_placa = entrada_placa_veiculo.get()
    criar_modelo = entrada_modelo_veiculo.get()
    criar_entrada = entrada_entrada_veiculo.get()
    criar_saida = entrada_saida_veiculo.get()
    criar_dono = entrada_dono_veiculo.get()


    if criar_placa.strip() == '' or criar_modelo.strip() == '' or criar_entrada.strip() == '' or criar_saida.strip() == '' or criar_dono.strip() == '':
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        criar_placa.focus()
    else:
        if placa_existe(criar_placa):
            messagebox.showerror("Erro", "Placa ja cadastrada!")
            entrada_placa_veiculo.delete(0, tk.END)
            criar_placa.focus()
        else:
            inserir_veiculo(criar_placa, criar_modelo, criar_entrada, criar_saida, criar_dono)
            messagebox.showinfo("Sucesso!","Novo cadastro de veiculo adicionado!")
            fechar_veiculo()
            adicionar_dado()
            buscar_tabela_veiculo()
        
def criar_menu():
    menubar = tk.Menu(tela)
    add_menu = tk.Menu(menubar,tearoff=0)

    menubar.add_cascade(label="Adicionar", menu=add_menu)
    
    tela.config(menu=menubar) 
    
    add_menu.add_command(label="Adicionar Usuário")
    add_menu.add_command(label="Remover Usuário")
    add_menu.add_command(label="Adicionar Login", command=adicionar_tela)
    add_menu.add_command(label="Remover Login", command=deletar_tela)
    add_menu.add_command(label="Log Out", command=voltar_tela_anterior)   

def botao_teste():
    global criar_login
    
    criar_login = entrada_usuario1.get()
    criar_senha = entrada_senha1.get()
    criar_nome = entrada_nome1.get()
    
    if criar_login.strip() == '' or criar_senha.strip() == '' or criar_nome.strip() == '':
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        criar_login.focus()
    else:
        if login_existe(criar_login):
            messagebox.showerror("Erro", "O login já existe")
            entrada_usuario1.delete(0, tk.END)
            entrada_senha1.delete(0, tk.END)
            criar_login.focus()
        else:
            inserir_dado(criar_login, criar_senha, criar_nome)
            messagebox.showinfo("Sucesso!","Novo login adicionado!")
            fechar_adicionar()

def botao_del_teste():
    global deletar_login
    
    deletar_login = usuario_del.get()
    
    if deletar_login.strip() == '':
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    elif login_existe(deletar_login):
        excluir_dado(usuario_del)
    else:
        messagebox.showerror("Erro!", "Usuario não existente. Digite novamente.")

def voltar_tela_anterior():
    tela_login.deiconify()
    tela.withdraw()

def adicionar_tela():
    global tela_adicionar, label5, igualsenha1, igualsenha2, botao2, botao3, entrada_usuario1, entrada_senha1, entrada_nome1, botao2, fechar_adicionar
    
    def fechar_adicionar():
        tela_adicionar.destroy()
    
    tela_adicionar = tk.Toplevel(master=tela)
    tela_adicionar.title("Adicionar Admin")
    tela_adicionar.geometry("400x300+700+200")
    tela_adicionar.resizable(0,0)
    tela_adicionar.transient(tela)
    
    entrada_senha1= tk.StringVar()
    entrada_nome1 = tk.StringVar()
    entrada_usuario1 = tk.StringVar()

    label5 = tk.Label(tela_adicionar, text="Usuário")
    label5.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entrada_usuario1 = tk.Entry(tela_adicionar)
    entrada_usuario1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    label6 = tk.Label(tela_adicionar, text="Senha")
    label6.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entrada_senha1 = tk.Entry(tela_adicionar)
    entrada_senha1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    label7 = tk.Label(tela_adicionar, text="Nome")
    label7.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    entrada_nome1 = tk.Entry(tela_adicionar)
    entrada_nome1.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    botao3 = tk.Button(tela_adicionar, text="Salvar", fg="#FFFFFF", width=10, height=1, bg="#215470", activebackground="#FFFFFF", command=botao_teste)
    botao3.place(relx=0.2, rely=0.8)

    botao3 = tk.Button(tela_adicionar, text="Cancelar", fg="#FFFFFF", width=10, height=1, command=fechar_adicionar, bg="#215470", activebackground="#FFFFFF")
    botao3.place(relx=0.6, rely=0.8)

def deletar_tela():
    global tela_deletar, botao_enter_del, resultado_del, usuario_del, entrada_usuario_del

    def pressionar_enter_delete(event):
        botao_enter_del.invoke()

    tela_deletar = tk.Toplevel(master=tela)
    tela_deletar.title("Deletando Usuário")
    tela_deletar.geometry("400x300+700+200")
    tela_deletar.resizable(0,0)
    tela_deletar.transient(tela)
    
    usuario_del = tk.StringVar()
    
    label_del_nome = tk.Label(tela_deletar, text="Digite o login do usuário:")
    label_del_nome.place(relx=0.25, rely=0.1, anchor=tk.CENTER)
    entrada_usuario_del = tk.Entry(tela_deletar, textvariable=usuario_del)
    entrada_usuario_del.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

    botao_enter_del = tk.Button(tela_deletar, text="Enter", fg="#FFFFFF", bg="#215470", activebackground="#FFFFFF", width=10, height=1, command=botao_del_teste)
    botao_enter_del.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    tela_deletar.bind('<Return>', pressionar_enter_delete)

criar_tela()
tela.withdraw()
login()
criar_menu()
tela.mainloop()