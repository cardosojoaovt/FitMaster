import flet as ft

# Dicionário de usuários simulados (para fins de demonstração)
usuarios = {
    "usuario@exemplo.com": {"senha": "12345"}
}

# Função para processar o login
def fazer_login(e, email_field, password_field, page):
    email = email_field.value
    senha = password_field.value
    
    if not email or not senha:
        page.dialog = ft.AlertDialog(title=ft.Text("E-mail e senha são obrigatórios."))
        page.dialog.open = True
        page.update()
        return
    
    usuario = usuarios.get(email)
    if usuario and usuario["senha"] == senha:
        abrir_tela_principal(page)
    else:
        page.dialog = ft.AlertDialog(title=ft.Text("E-mail ou senha incorretos."))
        page.dialog.open = True
        page.update()

# Função para criar uma nova conta (simulada, sem banco de dados)
def criar_conta(e, email_field, password_field, page):
    email = email_field.value
    senha = password_field.value
    
    if not email or not senha:
        page.dialog = ft.AlertDialog(title=ft.Text("E-mail e senha são obrigatórios."))
        page.dialog.open = True
        page.update()
        return
    
    if email in usuarios:
        page.dialog = ft.AlertDialog(title=ft.Text("Conta já existe."))
    else:
        usuarios[email] = {"senha": senha}
        page.dialog = ft.AlertDialog(title=ft.Text("Conta criada com sucesso!"))
    
    page.dialog.open = True
    page.update()

# Função para a tela principal após login bem-sucedido
def abrir_tela_principal(page):
    # Limpa a tela antes de exibir a nova tela principal
    page.controls.clear()

    # Botão de sair posicionado no canto superior esquerdo
    sair_button = ft.IconButton(
        icon=ft.icons.ARROW_BACK, 
        on_click=lambda e: abrir_tela_login(page), 
        icon_color="white",
    )

    # Texto de boas-vindas ao centro da tela
    bem_vindo_texto = ft.Text(
        "Bem-vindo à tela principal!", 
        color="white",
        size=24,
        weight=ft.FontWeight.
        
        BOLD,
        text_align="center"
    )

    # Estrutura de layout com o botão e o texto
    tela_principal = ft.Column(
        [
            ft.Row([sair_button], alignment=ft.MainAxisAlignment.START),
            ft.Row([bem_vindo_texto], alignment=ft.MainAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True
    )

    # Exibe o conteúdo da nova tela
    page.add(tela_principal)
    page.update()

# Função para exibir a tela de login
def abrir_tela_login(page):
    # Limpa a tela antes de exibir a tela de login
    page.controls.clear()

    email_field = ft.TextField(
        label="E-mail",
        hint_text="Digite seu e-mail",
        width=240,
    )

    password_field = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        password=True,
        width=240,
    )

    create_account = ft.TextButton("Criar conta", on_click=lambda e: criar_conta(e, email_field, password_field, page))
    forgot_password_button = ft.TextButton("Esqueci a minha senha", on_click=lambda e: ft.Toast("Função não implementada").show(page))
    login_button = ft.IconButton(
        icon=ft.icons.ARROW_FORWARD,
        bgcolor="#800080",
        icon_color="white",
        on_click=lambda e: fazer_login(e, email_field, password_field, page),
    )

    buttons_row = ft.Row(
        [create_account, forgot_password_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    logo = ft.Image(
        src="imagens/logoaplicativo.png",
        width=550,
        height=250
    )

    tela_login = ft.Column(
        [
            logo,
            email_field,
            password_field,
            buttons_row,
            login_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    page.add(tela_login)
    page.update()

# Função principal
def main(page: ft.Page):
    page.title = "Login - FitMaster"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window_width = 375
    page.window_height = 667
    page.bgcolor = "#2b0a3d"
    
    abrir_tela_login(page)

# Executa a aplicação
ft.app(target=main)
