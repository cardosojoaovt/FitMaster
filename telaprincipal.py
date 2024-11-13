import flet as ft
import sqlite3
import os

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
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

# Função para processar o login
def fazer_login(e, usuario_field, password_field, page):
    usuario = usuario_field.value
    senha = password_field.value
    
    if not usuario or not senha:
        page.dialog = ft.AlertDialog(title=ft.Text("Usuário e senha são obrigatórios."))
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
    cursor.execute('SELECT * FROM usuarios WHERE usuario = ? AND senha = ?', (usuario, senha))
    usuario = cursor.fetchone()
    
    if usuario:
        page.dialog = ft.AlertDialog(title=ft.Text("Login realizado com sucesso!"))
    else:
        page.dialog = ft.AlertDialog(title=ft.Text("Usuário ou senha incorretos."))
    
    page.dialog.open = True
    page.update()
    conn.close()

# Função para criar uma nova conta
def criar_conta(e, usuario_field, password_field, page):
    usuario = usuario_field.value
    senha = password_field.value
    
    if not usuario or not senha:
        page.dialog = ft.AlertDialog(title=ft.Text("Usuário e senha são obrigatórios."))
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
    cursor.execute('SELECT * FROM usuarios WHERE usuario = ?', (usuario,))
    usuario_existe = cursor.fetchone()
    
    if usuario_existe:
        page.dialog = ft.AlertDialog(title=ft.Text("Conta já existe."))
    else:
        cursor.execute('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', (usuario, senha))
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
    page.padding = 0
    page.window_width = 375
    page.window_height = 667
    page.bgcolor = "#2b0a3d"

    # Define o caminho para a logo
    logo_path = "logoaplicativo.png"
    if not os.path.exists(logo_path):
        print(f"Erro: Arquivo de logo não encontrado em '{logo_path}'")

    # Logo
    logo = ft.Image(
        src=logo_path,
        width=350,
        height=250
    )

    # Gradiente de fundo
    gradiente_inferior = ft.Container(
        width=page.window_width,
        height=page.window_height,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_center,
            end=ft.alignment.top_center,
            colors=["#000000", "transparent"],
        ),
    )

    # Campos de login
    usuario_field = ft.TextField(
        label="Usuário",
        hint_text="Digite seu nome de usuário",
        width=280,
    )

    password_field = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        password=True,
        width=280,
    )

    # Botões
    create_account = ft.TextButton("Criar conta", on_click=lambda e: criar_conta(e, usuario_field, password_field, page))
    login_button = ft.IconButton(
        icon=ft.icons.ARROW_FORWARD,
        bgcolor="#FF5722",
        icon_color="white",
        on_click=lambda e: fazer_login(e, usuario_field, password_field, page),
    )

    # Coluna com os campos de login e botões
    login_form = ft.Column(
        [
            ft.Container(content=logo, alignment=ft.alignment.center),  # Logo no topo
            usuario_field,
            password_field,
            ft.Row([create_account], alignment=ft.MainAxisAlignment.CENTER, width=280),
            login_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Organizando os elementos na tela com Stack
    page.add(
        ft.Stack(
            [
                gradiente_inferior,  # Gradiente como fundo
                login_form,          # Formulário de login sobre o gradiente
            ]
        )
    )

# Executa a aplicação
ft.app(target=main)
