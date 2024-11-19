import flet as ft

def main(pagina: ft.Page):
    nome_usuario = "JOÃO VITOR CARDOSO"
    
    # Configurações da página
    pagina.title = "FitMaster - Tela do Usuário"
    pagina.theme_mode = ft.ThemeMode.DARK
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.padding = 10
    pagina.window_width = 375
    pagina.window_height = 667
    pagina.bgcolor = "#2b0a3d"

    # Foto do usuário
    foto_usuario = ft.Image(
        src="imagens/usuario.png",
        width=100,
        height=100,
        color="#ffffff",
        fit=ft.ImageFit.COVER,
        border_radius=5,
    )

    # Nome do usuário
    nome_do_usuario = ft.Container(
        content=ft.Text(
            f"{nome_usuario}",
            size=18,
            color="#ffffff",
            weight=ft.FontWeight.BOLD,
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.symmetric(vertical=10),
    )

    # Blocos de interação com o app
    bloco_configuracoes = ft.Container(
        content=ft.Text(
            "Configurações do perfil",
            size=18,
            color="#ffffff",
            weight=ft.FontWeight.BOLD,
        ),
        width=250,
        height=50,
        bgcolor="purple",
        border_radius=5,
        alignment=ft.alignment.center,
        on_click=lambda e: print("Configurações do perfil clicado"),
    )

    bloco_perfil = ft.Container(
        content=ft.Text(
            "Ver meu perfil",
            size=18,
            color="#ffffff",
            weight=ft.FontWeight.BOLD,
        ),
        width=250,
        height=50,
        bgcolor="purple",
        border_radius=5,
        alignment=ft.alignment.center,
        on_click=lambda e: print("Perfil clicado"),
    )

    # Layout da tela
    pagina.add(
        foto_usuario,
        nome_do_usuario,
        ft.Column(
            controls=[
                bloco_configuracoes,
                bloco_perfil,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)
