import flet as ft

def TelaPulley(page: ft.Page, navegar_para):
    page.title = "Execução de Exercícios"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window.width = 375
    page.window.height = 667
<<<<<<< HEAD:Telas_Exercicios/tela_exercicios.py
    page.bgcolor = "#2b0a3d"

    # Criação da caixa de texto
=======
    page.bgcolor = "#5a0162"

>>>>>>> 3b4e1e78d4bfb489f19fb82d9a6beade62b495fd:telasExercicios/pulleyFrente.py
    text_box = [
        {"background_color": "#410f5d"}
    ]


    page.add(
       ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_color="white",
                    on_click=lambda e: navegar_para("ficha_treino"),  
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.symmetric(vertical=10),
    ),
    ft.Column(
            
            controls=[                  
                ft.Text("Pulley Frente", size=30, color="white", weight=ft.FontWeight.BOLD),
                ft.Container(
                padding=2 # Definindo um espaço vazio entre os elementos
            ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Execução", size=15, weight=ft.FontWeight.BOLD, color="white"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Alinha verticalmente o texto
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha horizontalmente o texto
                    ),
                    alignment=ft.alignment.center,  # Centraliza o conteúdo no container
                    width=110, height=40, bgcolor=text_box[0]["background_color"],  # Define a cor de fundo
                    border_radius=20
                ),
                ft.Container(
                padding=2 # Definindo um espaço vazio entre os elementos
            ),
                ft.Image(src="imagens/pulley_frente.gif", width=200, height=200, border_radius=15),  # Adiciona o GIF no centro
               
               ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Fortalecimento e hipertrofia da região das dorsais, abrange também, músculos auxiliares, tais como, trapézio e bíceps braquial.", 
                                    size=13, weight=ft.FontWeight, color="white"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Alinha verticalmente o texto
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha horizontalmente o texto
                    ),
                    alignment=ft.alignment.center,  # Centraliza o conteúdo no container
                    width=240, height=100),
               
               
                
                ft.Container(
                padding=2 # Definindo um espaço vazio entre os elementos
            ),
                ft.Container(
                    content=ft.Column( 
                        [
                            ft.Text("Região Trabalhada", size=15, weight=ft.FontWeight.BOLD, color="white"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Alinha verticalmente o texto
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha horizontalmente o texto
                    ),
                    alignment=ft.alignment.center,  # Centraliza o conteúdo no container
                    width=200, height=40, bgcolor=text_box[0]["background_color"],  # Define a cor de fundo
                    border_radius=20, 
                ),
                ft.Text("Costas / Dorsal", size=20, color="white", weight=ft.FontWeight),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
