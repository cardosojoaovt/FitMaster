from flet import *
import flet as ft

# Simulação de um banco de dados com usuários
usuarios = {
    "usuario@exemplo.com": {"senha": "12345"}
}

# ==================== Função Principal ====================
def main(pagina: ft.Page):
    pagina.title = "FitMaster - Tela de Login"
    pagina.theme_mode = ft.ThemeMode.DARK
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.padding = 20
    pagina.window_width = 375
    pagina.window_height = 667
    pagina.bgcolor = "#2b0a3d"  # Pode ser substituído por uma imagem de fundo

    abrir_tela_login(pagina)

# ==================== Tela de Login ====================
def abrir_tela_login(pagina):
    pagina.controls.clear()

    campo_email = ft.TextField(
        label="E-mail",
        bgcolor="#ffffff",
        hint_text="Digite seu e-mail",
        width=240,
    )
    campo_senha = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        bgcolor="#ffffff",
        password=True,
        can_reveal_password=True,
        width=240,
    )
    botao_criar_conta = ft.TextButton(
        "Criar conta",
        on_click=lambda _: criar_conta(campo_email.value, campo_senha.value, pagina),
    )
    botao_esqueci_senha = ft.TextButton(
        "Esqueci minha senha",
        on_click=lambda _: exibir_dialogo_redefinir_senha(pagina),
    )
    botao_login = ft.IconButton(
        icon=ft.icons.ARROW_FORWARD,
        bgcolor="#61188a",
        icon_color="white",
        on_click=lambda _: fazer_login(campo_email.value, campo_senha.value, pagina),
    )

    logo = ft.Image(src="imagens/logoaplicativo.png", width=300, height=150)

    # Estrutura da tela de login
    tela_login = ft.Column(
        [
            logo,
            campo_email,
            campo_senha,
            ft.Row(
                [botao_criar_conta, botao_esqueci_senha],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            botao_login,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    pagina.add(tela_login)
    pagina.update()

# ==================== Funções Auxiliares ====================
def exibir_alerta(mensagem, pagina):
    """Exibe uma mensagem de alerta."""
    pagina.dialog = ft.AlertDialog(title=ft.Text(mensagem), bgcolor="#410f5d")
    pagina.dialog.open = True
    pagina.update()

def exibir_snackbar(mensagem, pagina):
    """Exibe uma mensagem rápida no formato Snackbar."""
    pagina.snack_bar = ft.SnackBar(ft.Text(mensagem))
    pagina.snack_bar.open = True
    pagina.update()

# ==================== Redefinir Senha ====================
def redefinir_senha(email, nova_senha, pagina):
    if not email or not nova_senha:
        exibir_alerta("Por favor, preencha todos os campos.", pagina)
        return

    if email not in usuarios:
        exibir_alerta("E-mail não encontrado.", pagina)
    else:
        usuarios[email]["senha"] = nova_senha
        exibir_alerta("Senha redefinida com sucesso!", pagina)

def exibir_dialogo_redefinir_senha(pagina):
    """Exibe um diálogo para redefinir a senha."""
    campo_email = ft.TextField(
        label="E-mail",
        bgcolor="#ffffff",
        hint_text="Digite seu e-mail cadastrado",
    )
    campo_nova_senha = ft.TextField(
        label="Nova senha",
        bgcolor="#ffffff",
        hint_text="Digite a nova senha",
        password=True,
    )
    botao_confirmar = ft.TextButton(
        "Redefinir senha",
        on_click=lambda _: redefinir_senha(campo_email.value, campo_nova_senha.value, pagina),
    )

    dialogo = ft.AlertDialog(
        title=ft.Text("Redefinir senha"),
        bgcolor="#410f5d",
        content=ft.Column(
            [campo_email, campo_nova_senha],
            spacing=10,
            width=240,
        ),
        actions=[botao_confirmar],
    )

    pagina.dialog = dialogo
    dialogo.open = True
    pagina.update()

# ==================== Login ====================
def fazer_login(email, senha, pagina):
    if not email or not senha:
        exibir_alerta("Por favor, preencha o e-mail e a senha.", pagina)
        return

    usuario = usuarios.get(email)
    if usuario and usuario["senha"] == senha:
        abrir_telaprincipal(pagina)
    else:
        exibir_alerta("E-mail ou senha incorretos.", pagina)

# ==================== Criar Conta ====================
def criar_conta(email, senha, pagina):
    if not email or not senha:
        exibir_alerta("Por favor, preencha o e-mail e a senha.", pagina)
        return

    if email in usuarios:
        exibir_alerta("Essa conta já existe.", pagina)
    else:
        usuarios[email] = {"senha": senha}
        exibir_alerta("Conta criada com sucesso!", pagina)

# ==================== Tela Principal ====================
def abrir_telaprincipal(pagina):
    pagina.controls.clear()

    texto_bem_vindo = ft.Text("Bem-vindo à Tela Principal!", size=24, weight="bold")
    botao_logout = ft.ElevatedButton(
        text="Sair",
        bgcolor=ft.colors.RED,
        color=ft.colors.WHITE,
        on_click=lambda _: abrir_tela_login(pagina),
    )

    tela_principal = ft.Column(
        [texto_bem_vindo, botao_logout],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    pagina.add(tela_principal)
    pagina.update()

# ==================== Execução ====================
if __name__ == "__main__":
    ft.app(target=main)
