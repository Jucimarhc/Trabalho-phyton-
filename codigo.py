import tkinter as tk
from tkinter import messagebox
import sys
from banco import abrir_banco
from deletar import deletar_dado
from inserir import inserir_dado
from mudar import mudar_dado
from ver import ver_dado

def verificar_login():
    abrir_banco()

def testar():
    tela.withdraw()
    login()

def login():
    global tela_login, usuario_verify, senha_verify, entrada_usuario, entrada_senha, botao1, usuario, senha

    tela_login = tk.Toplevel(tela)
    tela_login.title("Login")
    tela_login.geometry("400x300+500+200")
    tela_login.resizable(False, False)

    usuario_verify = tk.StringVar()
    senha_verify = tk.StringVar()

    label2 = tk.Label(tela_login, text="Usuário", bg="White")
    label2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entrada_usuario = tk.Entry(tela_login, textvariable=usuario_verify)
    entrada_usuario.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    entrada_usuario.focus()
    label3 = tk.Label(tela_login, text="Senha", bg="White")
    label3.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entrada_senha = tk.Entry(tela_login, textvariable=senha_verify, show='*')
    entrada_senha.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    botao1 = tk.Button(tela_login, text="Login", width=10, height=1, command=verificar_login)
    botao1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    tela_login.bind('<Return>', pressionar_enter)
    tela_login.protocol("WM_DELETE_WINDOW", fechar)
    
def pressionar_enter(event):
    botao1.invoke()

def pressionar_enter1(event):
    botao2.invoke()

def attframewallpaper_login(event):
    global wallpaper_login, label4
    
    largura = event.width
    altura = event.height
    
    label4.configure(image=wallpaper_login)

def fechar():
    tela_login.destroy()
    sys.exit()

def criar_tela():
    global tela, wallpaper
    tela = tk.Tk()
    tela.geometry("1600x900")
    tela.resizable(False,False)
    tela.title("RAD")

def fechar_adicionar():
    tela_adicionar.destroy()
   
def criar_menu():
   
    menubar = tk.Menu(tela)
    arquivo_menu = tk.Menu(menubar,tearoff=0)
    editar_menu = tk.Menu(menubar,tearoff=0)
    ferramentas_menu = tk.Menu(menubar,tearoff=0)
    opcoes_menu = tk.Menu(menubar,tearoff=0)
    sobre_menu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Arquivo", menu=arquivo_menu)
    menubar.add_cascade(label="Opções", menu=opcoes_menu)
    tela.config(menu=menubar) 
    arquivo_menu.add_command(label="Novo  Ctrl+Shift+N")
    arquivo_menu.add_command(label="Abrir  Ctrl+O")
    arquivo_menu.add_command(label="Salvar  Ctrl+S")
    opcoes_menu.add_command(label="Idioma")
    opcoes_menu.add_command(label="Config")
    opcoes_menu.add_command(label="Editar")
    opcoes_menu.add_command(label="Adicionar", command=adicionar_tela)

def botao2teste():
    login = entrada_usuario1.get()
    senha = entrada_senha1.get()
    nome = entrada_nome1.get()
    inserir_dado(login, senha, nome)




def adicionar_tela():
    
    global tela_adicionar, label5, igualsenha1, igualsenha2, botao2, botao3, entrada_usuario1, entrada_senha1, entrada_nome1, botao2
    tela_adicionar = tk.Toplevel(master=tela)
    tela_adicionar.title("Adicionando Usuário")
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

    botao2 = tk.Button(tela_adicionar, text="Salvar", width=10, height=1, bg="#80ff80", activebackground="#b3ffb3", command=botao2teste)
    botao2.place(relx=0.2, rely=0.8)

    tela_adicionar.bind('<Return>', pressionar_enter1)

    botao3 = tk.Button(tela_adicionar, text="Cancelar", width=10, height=1, command=fechar_adicionar, bg="#ff3333", activebackground="#ff6666")
    botao3.place(relx=0.6, rely=0.8)


criar_tela()
login()
criar_menu()
tela.mainloop()
