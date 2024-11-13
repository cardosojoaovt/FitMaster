import flet as ft

# Dicionário de usuários
usuarios = {
    "usuario@exemplo.com": {"senha": "12345"}
}

# Função para processar o login
def fazer_login(e, email_field, password_field, page):
    email = email_field.value
    senha = password_field.value
    
    if not email or not senha:  # Verifica se os campos estão vazios
        page.dialog = ft.AlertDialog(title=ft.Text("E-mail e senha são obrigatórios."))
        page.dialog.open = True
        page.update()
        return
    
    # Verifica se o e-mail existe e se a senha está correta
    usuario = usuarios.get(email)
    if usuario and usuario["senha"] == senha:
        page.dialog = ft.AlertDialog(title=ft.Text("Login realizado com sucesso!"))
    else:
        page.dialog = ft.AlertDialog(title=ft.Text("E-mail ou senha incorretos."))
    
    page.dialog.open = True
    page.update()

# Função para criar uma nova conta (simulada, sem banco de dados)
def criar_conta(e, email_field, password_field, page):
    email = email_field.value
    senha = password_field.value
    
    if not email or not senha:  # Verifica se os campos estão vazios
        page.dialog = ft.AlertDialog(title=ft.Text("E-mail e senha são obrigatórios."))
        page.dialog.open = True
        page.update()
        return
    
    # Verifica se o e-mail já existe
    if email in usuarios:
        page.dialog = ft.AlertDialog(title=ft.Text("Conta já existe."))
    else:
        # Cria o novo usuário no dicionário
        usuarios[email] = {"senha": senha}
        page.dialog = ft.AlertDialog(title=ft.Text("Conta criada com sucesso!"))
    
    page.dialog.open = True
    page.update()

# Função para o botão "Esqueci a minha senha"
def esqueci_senha(e, page):
    # Cria o campo para o novo e-mail
    email_field = ft.TextField(label="Digite seu e-mail", hint_text="Novo e-mail", width=240)
    
    # Função para verificar o e-mail e permitir a mudança de senha
    def verificar_email(e):
        novo_email = email_field.value
        
        if not novo_email:  # Verifica se o campo de e-mail está vazio
            page.dialog = ft.AlertDialog(title=ft.Text("Por favor, digite o seu e-mail."))
            page.dialog.open = True
            page.update()
            return
        
        # Verifica se o e-mail existe
        if novo_email in usuarios:
            # Se o e-mail existir, permite que o usuário altere a senha
            nova_senha_field = ft.TextField(label="Nova Senha", hint_text="Digite sua nova senha", password=True, width=240)
            
            def atualizar_senha(e):
                nova_senha = nova_senha_field.value
                
                if not nova_senha:  # Verifica se o campo de nova senha está vazio
                    page.dialog = ft.AlertDialog(title=ft.Text("Por favor, digite a nova senha."))
                    page.dialog.open = True
                    page.update()
                    return
                
                # Atualiza a senha no dicionário
                usuarios[novo_email]["senha"] = nova_senha
                page.dialog = ft.AlertDialog(title=ft.Text("Senha atualizada com sucesso!"))
                page.dialog.open = True
                page.update()

            # Exibe o campo de nova senha e o botão para atualizar
            page.dialog = ft.AlertDialog(
                title=ft.Text("Recuperação de Senha"),
                content=ft.Column([nova_senha_field], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                actions=[ft.TextButton("Atualizar Senha", on_click=atualizar_senha)]
            )
        else:
            # Se o e-mail não for encontrado, exibe um erro
            page.dialog = ft.AlertDialog(title=ft.Text("E-mail não encontrado."))
            page.dialog.open = True
            page.update()
        
        page.dialog.open = True
        page.update()

    # Exibe o campo de e-mail e o botão para verificar
    page.dialog = ft.AlertDialog(
        title=ft.Text("Recuperação de Senha"),
        content=ft.Column([email_field], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        actions=[ft.TextButton("Verificar E-mail", on_click=verificar_email)],
    )
    
    page.dialog.open = True
    page.update()

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
        width=240,  # Tamanho mais compacto
    )

    # Campo de senha
    password_field = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        password=True,
        width=240,  # Tamanho mais compacto
    )

    # Botões de ação
    create_account = ft.TextButton("Criar conta", on_click=lambda e: criar_conta(e, email_field, password_field, page))
    forgot_password_button = ft.TextButton(
        "Esqueci a minha senha",
        on_click=lambda e: esqueci_senha(e, page)
    )
    login_button = ft.IconButton(
        icon=ft.icons.ARROW_FORWARD,
        bgcolor="#800080",
        icon_color="white",
        on_click=lambda e: fazer_login(e, email_field, password_field, page),
    )

    # Organiza os botões "Criar conta" e "Esqueci a minha senha" na mesma linha
    buttons_row = ft.Row(
        [create_account, forgot_password_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,  # Espaçamento entre os botões
    )

    # Adiciona os elementos na página
    page.add(
        logo,
        email_field,
        password_field,
        buttons_row,  # Linha com os botões de criar conta e esqueci a senha
        login_button,
    )

ft.app(target=main)
