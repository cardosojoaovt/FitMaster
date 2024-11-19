import flet as ft

# Simulação de um banco de dados com usuários
usuarios = {
    "usuario@exemplo.com": {"senha": "12345"}
}

# Exibe mensagens de alerta
def exibir_alerta(titulo, pagina):
    pagina.dialog = ft.AlertDialog(title=ft.Text(titulo))
    pagina.dialog.open = True
    pagina.update()

# Exibe mensagens rápidas
def exibir_snackbar(mensagem, pagina):
    pagina.snack_bar = ft.SnackBar(ft.Text(mensagem))
    pagina.snack_bar.open = True
    pagina.update()

# Redefinir senha
def redefinir_senha(email, nova_senha, pagina):
    if not email or not nova_senha:
        exibir_alerta("Por favor, preencha todos os campos.", pagina)
        return

    if email not in usuarios:
        exibir_alerta("E-mail não encontrado.", pagina)
    else:
        usuarios[email]["senha"] = nova_senha
        exibir_alerta("Senha redefinida com sucesso!", pagina)

# Dialog de "Esqueci minha senha"
def exibir_dialogo_redefinir_senha(pagina):
    campo_email = ft.TextField(label="E-mail", hint_text="Digite seu e-mail cadastrado")
    campo_nova_senha = ft.TextField(label="Nova senha", hint_text="Digite a nova senha", password=True)

    botao_confirmar = ft.TextButton(
        "Redefinir senha",
        on_click=lambda evento: redefinir_senha(campo_email.value, campo_nova_senha.value, pagina)
    )

    dialogo = ft.AlertDialog(
        title=ft.Text("Redefinir senha"),
        content=ft.Column(
            [campo_email, campo_nova_senha],
            spacing=10,
        ),
        actions=[botao_confirmar],
    )

    pagina.dialog = dialogo
    dialogo.open = True
    pagina.update()

# Login
def fazer_login(email, senha, pagina):
    if not email or not senha:
        exibir_alerta("Por favor, preencha o e-mail e a senha.", pagina)
        return

    usuario = usuarios.get(email)
    if usuario and usuario["senha"] == senha:
        abrir_tela_principal(pagina)
    else:
        exibir_alerta("E-mail ou senha incorretos.", pagina)

# Criar conta
def criar_conta(email, senha, pagina):
    if not email or not senha:
        exibir_alerta("Por favor, preencha o e-mail e a senha.", pagina)
        return

    if email in usuarios:
        exibir_alerta("Essa conta já existe.", pagina)
    else:
        usuarios[email] = {"senha": senha}
        exibir_alerta("Conta criada com sucesso!", pagina)

# Tela principal
def abrir_tela_principal(pagina):
    pagina.controls.clear()

    botao_sair = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        on_click=lambda evento: abrir_tela_login(pagina),
        icon_color="white",
    )

    mensagem_bem_vindo = ft.Text(
        "Bem-vindo à tela principal!",
        color="white",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align="center"
    )

    # Column para organizar os itens
    tela_principal = ft.Column(
        [
            ft.Row([botao_sair], alignment=ft.MainAxisAlignment.START),
            ft.Row([mensagem_bem_vindo], alignment=ft.MainAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True
    )

    pagina.add(tela_principal)
    pagina.update()

# Tela de login
def abrir_tela_login(pagina):
    pagina.controls.clear()
    campo_email = ft.TextField(label="E-mail", hint_text="Digite seu e-mail", width=240,)
    campo_senha = ft.TextField(label="Senha", hint_text="Digite sua senha", password=True, width=240)

    botao_criar_conta = ft.TextButton(
        "Criar conta",
        on_click=lambda evento: criar_conta(campo_email.value, campo_senha.value, pagina)
    )
    botao_esqueci_senha = ft.TextButton(
        "Esqueci minha senha",
        on_click=lambda evento: exibir_dialogo_redefinir_senha(pagina)
    )
    botao_login = ft.IconButton(
        icon=ft.icons.ARROW_FORWARD,
        bgcolor="#800080",
        icon_color="white",
        on_click=lambda evento: fazer_login(campo_email.value, campo_senha.value, pagina),
    )

    logo = ft.Image(src="imagens/logoaplicativo.png", width=300, height=150)

    # Column e Row para organizar a tela de login
    tela_login = ft.Column(
        [
            logo,
            campo_email,
            campo_senha,
            ft.Row([botao_criar_conta, botao_esqueci_senha], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            botao_login,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    pagina.add(tela_login)
    pagina.update()

# Função principal
def main(pagina: ft.Page):
    pagina.title = "FitMaster - Tela de Login"
    pagina.theme_mode = ft.ThemeMode.DARK
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.padding = 20
    pagina.window_width = 375
    pagina.window_height = 667
    pagina.bgcolor = "#2b0a3d"  # Pode ser substituído por uma imagem de fundo, se preferir

    abrir_tela_login(pagina)

if __name__ == "__main__":
    ft.app(target=main)
