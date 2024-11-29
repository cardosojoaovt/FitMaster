import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Execução de Exercícios"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window.width = 375
    page.window.height = 667
    page.bgcolor = "#2b0a3d"

    
    

    # Criação da caixa de texto
    text_box = [
        {"background_color": "purple"}
    ]

    # Layout tela de exercicios
    page.add(
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Image(src="imagens/voltar.png", width=35, height=35, border_radius=10),
                        ],
                    ),
                    alignment=ft.alignment.top_left, on_click="", # Função de clique do botão
                    
                            )
                    ]  
                ),
            
    ft.Column(
            
            controls=[                  
                ft.Text("Crucifixo", size=30, color="white", weight=ft.FontWeight.BOLD),
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
                ft.Image(src="imagens/crucifixo.gif", width=200, height=200, border_radius=15),  # Adiciona o GIF no centro
               
               ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Fortalecimento e hipertrofia dos músculos peitorais, com enfoque aos músculos peitoral maior e menor. Estimula a coordenação motora.", 
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
                ft.Text("Peitoral", size=20, color="white", weight=ft.FontWeight),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
# Executa o aplicativo Flet
ft.app(target=main)
