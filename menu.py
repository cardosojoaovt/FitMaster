from flet import *
import flet as ft

def TelaMenu(page: ft.Page, navegar_para, *args):
    page.title = "FitMaster - Menu"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_width = 375
    page.window_height = 667
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#2b0a3d"
    page.scroll = 'auto'

    def mostrar_menu():
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Menu", size=30, color="white", weight=ft.FontWeight.BOLD),
                    *menu_widgets,
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    def navegar_ficha_treino(e):
        navegar_para("ficha_treino")


    def navegar_avaliacoes(e):
        mostrar_tela_avaliacoes()

    def navegar_seu_plano(e):
        navegar_para("plano")

    def navegar_perfil(e):
        navegar_para("usuario")

    def mostrar_tela_avaliacoes():
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_color="white",
                                    on_click=lambda e: mostrar_menu(),
                                ),
                                ft.Text(
                                    "Avaliações",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=ft.padding.symmetric(horizontal=10, vertical=15),
                        bgcolor="#410f5d",
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.LOCAL_HOSPITAL, color="white", size=24),
                                ft.Text(
                                    "Avaliação - 15/10/2024",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        border_radius=10,
                        padding=15,
                        bgcolor="#410f5d",
                        height=60,
                        margin=ft.margin.symmetric(vertical=10),
                        on_click=lambda e: mostrar_detalhes_avaliacao(),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    def mostrar_detalhes_avaliacao():
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_color="white",
                                    on_click=lambda e: mostrar_tela_avaliacoes(),
                                ),
                                ft.Text(
                                    "Detalhes da Avaliação",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=ft.padding.symmetric(horizontal=10, vertical=15),
                        bgcolor="#410f5d",
                    ),
                    ft.Text("Detalhes da avaliação aqui...", size=18, color="white"),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    menu_items = [
        {
            "label": "FICHA DE TREINO",
            "subtext": "Visualizar dados",
            "action": navegar_ficha_treino,
            "image": "imagens/fichadetreino.png",
        },
        {
            "label": "AVALIAÇÕES FÍSICAS",
            "subtext": "Consultar resultados",
            "action": navegar_avaliacoes,
            "image": "imagens/avaliacao.png",
        },
        {
            "label": "SEU PLANO",
            "subtext": "Informações do plano",
            "action": navegar_seu_plano,
            "image": "imagens/seuplano.png",
        },
        {
            "label": "PERFIL",
            "subtext": "Editar dados do perfil",
            "action": navegar_perfil,
            "image": "imagens/perfil.png",
        },
    ]

    menu_widgets = [
        ft.Container(
            content=ft.Stack(
                [
                    ft.Image(
                        src=item["image"], fit=ft.ImageFit.COVER, width=350, height=100
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    item["label"],
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),
                                ft.Text(item["subtext"], color="lightgray"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=10,
                        alignment=ft.alignment.center,
                    ),
                ]
            ),
            border_radius=5,
            on_click=item["action"],
            width=350,
            height=100,
        )
        for item in menu_items
    ]

    mostrar_menu()
