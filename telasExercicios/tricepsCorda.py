import flet as ft

def TelaTricepsCorda(page: ft.Page, navegar_para):
    page.title = "Execução de Exercícios"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window.width = 375
    page.window.height = 667
    page.bgcolor = "#2b0a3d"

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
                ft.Text("Triceps Corda", size=30, color="white", weight=ft.FontWeight.BOLD),
                
                ft.Container(
                    padding=2
                ),
                
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Execução", size=15, weight=ft.FontWeight.BOLD, color="white"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    alignment=ft.alignment.center,
                    width=110, height=40, bgcolor=text_box[0]["background_color"],
                    border_radius=20
                ),
                
                ft.Container(
                    padding=2
                ),
                
                ft.Image(src="imagens/triceps_corda.gif", width=200, height=200, border_radius=15),
                
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Exercício para fortalecimento e hipertrofia dos músculos tríceps, com enfoque no tríceps braquial.", 
                                    size=13, weight=ft.FontWeight, color="white"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    alignment=ft.alignment.center,
                    width=240, height=100,
                ),
               
                ft.Container(
                    padding=2
                ),
                
                ft.Container(
                    content=ft.Column( 
                        [
                            ft.Text("Região Trabalhada", size=15, weight=ft.FontWeight.BOLD, color="white"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    alignment=ft.alignment.center,
                    width=200, height=40, bgcolor=text_box[0]["background_color"],
                    border_radius=20, 
                ),
                
                ft.Text("Tríceps", size=20, color="white", weight=ft.FontWeight),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
