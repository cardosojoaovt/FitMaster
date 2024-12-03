from flet import *
import flet as ft

def TelaPlano(page: ft.Page, navegar_para):
    page.title = "Meu Plano"
    page.bgcolor = "#2b0a3d"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    page.window.width = 375
    page.window.height = 667
    page.theme_mode = ft.ThemeMode.DARK

    plano_atual = "PLANO GOLD"

    def on_back_button_click(e):
        navegar_para("menu")

    def show_plan_options(e):
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
                padding=10,
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

    info_text = ft.Text("Seu plano atual é o:", style=ft.TextStyle(color="white", size=16))
    plano_text = ft.Text(plano_atual, style=ft.TextStyle(color="yellow", size=30, weight=ft.FontWeight.BOLD))
    preco_text = ft.Text("R$ 89,90/mês", style=ft.TextStyle(color="white", size=14))
    trocar_plano_button = ft.ElevatedButton(
        text="Trocar de Plano",
        on_click=show_plan_options,
        width=200,
        height=50,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREY_200,
            color="black",
        ),
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_color="white",
                            on_click=on_back_button_click,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Text("Seu plano", style=ft.TextStyle(color="white", size=24, weight=ft.FontWeight.BOLD)),
                info_text,
                plano_text,
                preco_text,
                trocar_plano_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
    )
