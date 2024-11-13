import flet as ft
import sqlite3

# Função para conectar ao banco de dados
def conectar_banco():
    try:
        return sqlite3.connect('fitmaster.db')
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para criar a tabela de usuários, caso não exista
def criar_tabela():
    conn = conectar_banco()
    if conn is None:
        print("Erro ao conectar ao banco de dados.")
        return
    
    cursor = conn.cursor()

    # Cria a tabela usuarios se ela não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    );
    ''')

    conn.commit()
    conn.close()

# Função para processar o login
def fazer_login(e, email_field, password_field, page):
    email = email_field.value
    senha = password_field.value
    
    if not email or not senha:  # Verifica se os campos estão vazios
        page.dialog = ft.AlertDialog(title=ft.Text("E-mail e senha são obrigatórios."))
        page.dialog.open = True
        page.update()
        return
    
    conn = conectar_banco()
    if conn is None:
        page.dialog = ft.AlertDialog(title=ft.Text("Erro ao conectar ao banco de dados"))
        page.dialog.open = True
        page.update()
        return
    
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', (email, senha))
    usuario = cursor.fetchone()  # Pega o primeiro resultado encontrado
    
    if usuario:
        page.dialog = ft.AlertDialog(title=ft.Text("Login realizado com sucesso!"))
    else:
        page.dialog = ft.AlertDialog(title=ft.Text("E-mail ou senha incorretos."))
    
    page.dialog.open = True
    page.update()
    conn.close()

# Função para criar uma nova conta
def criar_conta(e, email_field, password_field, page):
    email = email_field.value
    senha = password_field.value
    
    if not email or not senha:  # Verifica se os campos estão vazios
        page.dialog = ft.AlertDialog(title=ft.Text("E-mail e senha são obrigatórios."))
        page.dialog.open = True
        page.update()
        return
    
    conn = conectar_banco()
    if conn is None:
        page.dialog = ft.AlertDialog(title=ft.Text("Erro ao conectar ao banco de dados"))
        page.dialog.open = True
        page.update()
        return
    
    cursor = conn.cursor()
    
    # Verifica se o e-mail já existe
    cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
    usuario = cursor.fetchone()
    
    if usuario:
        page.dialog = ft.AlertDialog(title=ft.Text("Conta já existe."))
    else:
        # Cria o novo usuário
        cursor.execute('INSERT INTO usuarios (email, senha) VALUES (?, ?)', (email, senha))
        conn.commit()
        page.dialog = ft.AlertDialog(title=ft.Text("Conta criada com sucesso!"))
    
    page.dialog.open = True
    page.update()
    conn.close()

# Chama a função para criar a tabela ao iniciar o aplicativo
criar_tabela()

def main(page: ft.Page):
    page.title = "Login - FitMaster"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window.width = 375
    page.window.height = 667
    page.bgcolor = "#2b0a3d"
    
    # Logo
    logo = ft.Image(
        src="imagens/logoaplicativo.png",  # Substitua pelo caminho correto da logo
        width=550,
        height=250
    )

    # Campo de e-mail
    email_field = ft.TextField(
        label="E-mail",
        hint_text="Digite seu e-mail",
        width=280,
    )

    # Campo de senha
    password_field = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        password=True,
        width=280,
    )

    # Botões de ação
    create_account = ft.TextButton("Criar conta", on_click=lambda e: criar_conta(e, email_field, password_field, page))
    login_button = ft.IconButton(
        icon=ft.icons.ARROW_FORWARD,
        bgcolor="#FF5722",
        icon_color="white",
        on_click=lambda e: fazer_login(e, email_field, password_field, page),
    )

    # Adiciona os elementos na página
    page.add(
        logo,
        email_field,
        password_field,
        ft.Row([create_account], alignment=ft.MainAxisAlignment.CENTER, width=280),
        login_button,
    )

ft.app(target=main)
