from flet import *
import flet as ft

def principal(page: ft.Page):
    page.title = "FitMaster - Menu"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window.width = 375
    page.window.height = 667
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centraliza o conteúdo verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centraliza o conteúdo horizontalmente
    page.bgcolor = "#2b0a3d"
    page.scroll = 'auto'
    page.appbar = AppBar(bgcolor="#410f5d")

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

    # Calculo do IMC
    def calcular_imc(peso, altura):
        try:
            imc = round(peso / (altura ** 2), 2)
            return f"{imc} (Normal)" if 18.5 <= imc < 25 else f"{imc} (Fora do Normal)"
        except:
            return "Erro no cálculo"

    # Menu do calculo IMC
    def menu_calculo_imc(e):
        peso_field = ft.TextField(label="Peso (kg)", width=200, bgcolor="#ffffff", color="black")
        altura_field = ft.TextField(label="Altura (m)", width=200, bgcolor="#ffffff", color="black")

        def calcular_e_mostrar_imc(e):
            try:
                peso = float(peso_field.value)
                altura = float(altura_field.value)
                imc = calcular_imc(peso, altura)
                resultado_text.value = f"IMC: {imc}"
                page.update()
            except ValueError:
                resultado_text.value = "Por favor, insira valores válidos."
                page.update()

        resultado_text = ft.Text(color="white")

        page.dialog = ft.AlertDialog(
            title=ft.Text("Calcular IMC", size=24, weight=ft.FontWeight.BOLD, color="white"),
            content=ft.Column([
                peso_field,
                altura_field,
                ft.ElevatedButton(text="Calcular", on_click=calcular_e_mostrar_imc),
                resultado_text
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            on_dismiss=lambda e: page.update(),
            bgcolor="#410f5d",
        )
        page.dialog.open = True
        page.update()

    # Tela de detalhes da avaliação
    def mostrar_detalhes_avaliacao(e):
        page.controls.clear()

        dados_avaliacao = [
            ("Data", "15/10/2024"),
            ("Peso", "70 kg"),
            ("Altura", "1.75 m"),
            ("IMC", ft.ElevatedButton(text="Fazer cálculo",color= "white", on_click=menu_calculo_imc)),
            ("Gordura Corporal", "18%"),
            ("Massa Magra", "57 kg"),
            ("Frequência Cardíaca", "72 bpm"),
            ("Pressão Arterial", "120/80 mmHg"),
        ]

        page.add(
            ft.Column(
                controls=[
                    # Título fixo no topo
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_color="white",
                                    on_click=lambda e: mostrar_tela_avaliacoes(e),
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
                    # Exibir os dados da avaliação
                    *[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        chave,
                                        size=18,
                                        color="white",
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    valor if isinstance(valor, ft.Control) else ft.Text(
                                        valor,
                                        size=18,
                                        color="lightgray",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            padding=ft.padding.all(10),
                            bgcolor="#410f5d",
                            border_radius=10,
                            margin=ft.margin.symmetric(vertical=5),
                        )
                        for chave, valor in dados_avaliacao
                    ],
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    # Tela de Avaliações
    def mostrar_tela_avaliacoes(e):
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
                        on_click=mostrar_detalhes_avaliacao,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    def mostrar_ficha_treino(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("FICHA DE TREINO", size=24, weight=ft.FontWeight.BOLD, color="white"),
            content=ft.Text("VIZUALIZAR EXERCÍCIOS.", size=18, color="lightgray"),
            on_dismiss=lambda e: page.update(),
            bgcolor="#410f5d",
        )
        page.dialog.open = True
        page.update()

    def mostrar_produtos(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("PRODUTOS", size=24, weight=ft.FontWeight.BOLD, color="white"),
            content=ft.Text("LOJA DE PRODUTOS E SUPLEMEMENTOS.", size=18, color="lightgray"),
            on_dismiss=lambda e: page.update(),
            bgcolor="#410f5d",
        )
        page.dialog.open = True
        page.update()

    def mostrar_seu_plano(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("SEU PLANO", size=24, weight=ft.FontWeight.BOLD, color="white"),
            content=ft.Text("INFORMAÇÕES DO SEU PLANO.", size=18, color="lightgray"),
            on_dismiss=lambda e: page.update(),
            bgcolor="#410f5d",
        )
        page.dialog.open = True
        page.update()

    def mostrar_perfil(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("PERFIL", size=24, weight=ft.FontWeight.BOLD, color="white"),
            content=ft.Text("EDITAR DADOS DO PERFIL.", size=18, color="lightgray"),
            on_dismiss=lambda e: page.update(),
            bgcolor="#410f5d",
        )
        page.dialog.open = True
        page.update()

    menu_items = [
        {
            "label": "FICHA DE TREINO",
            "subtext": "VIZUALIZAR DADOS",
            "action": mostrar_ficha_treino,
            "image": "imagens/fichadetreino.png",
        },
        {
            "label": "PRODUTOS",
            "subtext": "LOJA",
            "action": mostrar_produtos,
            "image": "imagens/loja.png",
        },
        {
            "label": "AVALIAÇÕES FISICAS",
            "subtext": "CONSULTAR RESULTADOS",
            "action": mostrar_tela_avaliacoes,
            "image": "imagens/avaliação.png",
        },
        {
            "label": "SEU PLANO",
            "subtext": "INFORMAÇÕES",
            "action": mostrar_seu_plano,
            "image": "imagens/seuplano.png",
        },
        {
            "label": "Perfil",
            "subtext": "EDITAR DADOS DO PERFIL",
            "action": mostrar_perfil,
            "image": "imagens/perfil.png",
        },
    ]

    menu_widgets = []
    for item in menu_items:
        menu_widgets.append(
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
        )

    mostrar_menu()

ft.app(target=principal)
