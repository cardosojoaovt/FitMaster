from flet import *
import flet as ft

def main(page: ft.Page):
    page.title = "Meu Plano"
    page.bgcolor = "#2b0a3d"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centraliza o conteúdo verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centraliza o conteúdo horizontalmente
    page.padding = 0

    page.window.width = 375
    page.window.height = 667
    page.theme_mode = ft.ThemeMode.DARK

    plano_atual = "PLANO GOLD"

    back_icon = ft.Image(src="imagens/seta_voltar.png", width=30, height=30)

    def on_back_button_click(e):
        page.go_back()

    def show_plan_options(e):
        # Cria o diálogo com as opções de plano
        dialog = ft.AlertDialog(
            title=ft.Text("Escolha um Plano", style=ft.TextStyle(color="white", size=18)),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text("PLANO GOLD - R$ 89,90/mês", style=ft.TextStyle(color="white", size=14)),
                                ft.ElevatedButton("Selecionar", on_click=lambda _: select_plan("PLANO GOLD"), width=120),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Row(
                            controls=[
                                ft.Text("PLANO BÁSICO - R$ 49,90/mês", style=ft.TextStyle(color="white", size=14)),
                                ft.ElevatedButton("Selecionar", on_click=lambda _: select_plan("PLANO BÁSICO"), width=120),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    ],
                    spacing=8,
                ),
                padding=10,  # Ajuste para aumentar o espaço interno da caixa
            ),
            actions=[ft.TextButton("Fechar", on_click=lambda _: close_dialog(dialog))],
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    def close_dialog(dialog):
        dialog.open = False
        page.update()

    def select_plan(selected_plan):
        nonlocal plano_atual
        plano_atual = selected_plan
        plano_text.value = plano_atual
        preco_text.value = "R$ 89,90/mês" if plano_atual == "PLANO GOLD" else "R$ 49,90/mês"
        page.update()

    # Criando os textos e botões
    info_text = ft.Text("Seu plano atual é o:", style=ft.TextStyle(color="white", size=16))
    plano_text = ft.Text(plano_atual, style=ft.TextStyle(color="yellow", size=30, weight=ft.FontWeight.BOLD))
    preco_text = ft.Text("R$ 89,90/mês", style=ft.TextStyle(color="white", size=14))
    trocar_plano_button = ft.ElevatedButton(
        text="Trocar de Plano",
        on_click=show_plan_options,
        width=200,  # Largura aumentada
        height=50,  # Altura ajustada
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREY_200,  # Cor cinza claro corrigida
            color="black",  # Texto em preto para contraste
        ),
    )

    page.add(
        ft.Column(
            controls=[
                # Seta de voltar à esquerda com margem ajustada
                ft.Container(
                    content=ft.Row(
                        controls=[back_icon],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    padding=ft.Padding(top=-80, left=0, right=50, bottom=0),
                ),
                # Contêiner "Seu plano"
                ft.Container(
                    content=ft.Text("Seu plano", style=ft.TextStyle(color="white", size=24, weight=ft.FontWeight.BOLD)),
                    padding=ft.Padding(top=-90, left=0, right=0, bottom=0),
                ),
                # Contêiner "Seu plano atual é o:"
                ft.Container(
                    content=info_text,
                    padding=ft.Padding(top=120, left=0, right=0, bottom=0),
                ),
                # Contêiner "PLANO GOLD" amarelo
                ft.Container(
                    content=plano_text,
                    padding=ft.Padding(top=40, left=0, right=0, bottom=0),
                ),
                # Contêiner "R$ 89,90/mês"
                ft.Container(
                    content=preco_text,
                    padding=ft.Padding(top=5, left=0, right=0, bottom=0),
                ),
                # Contêiner botão "Trocar de plano"
                ft.Container(
                    content=trocar_plano_button,
                    padding=ft.Padding(top=110, left=0, right=0, bottom=0),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
    )

ft.app(target=main)
