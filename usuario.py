from flet import *
import flet as ft

def TelaUsuario(page: ft.Page, navegar_para):
    page.title = "Usuário"
    page.bgcolor = "#2b0a3d"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window_width = 375
    page.window_height = 667
    page.theme_mode = ft.ThemeMode.DARK

    profile_image = "imagens/usuario.png" 

    def change_profile_image(e):
        if file_picker.result and file_picker.result.files:
            new_image = file_picker.result.files[0].path
            nonlocal profile_image
            profile_image = new_image
            show_profile_section()

    def show_profile_section():
        page.clean() 
        page.add(
            ft.Column(
                controls=[
                    
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_size=24,
                                    bgcolor="#410f5d",
                                    icon_color="white",
                                    tooltip="Voltar",
                                    on_click=lambda e: navegar_para("menu"), 
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        padding=ft.Padding(left=10, top=10, right=10, bottom=10),  
                    ),
                    
                    ft.Stack(
                        controls=[
                            ft.Container(
                                content=ft.Image(
                                    src=profile_image,
                                    width=120,
                                    height=120,
                                    fit="cover",
                                    border_radius=60,
                                ),
                                padding=10,
                                alignment=alignment.center,
                            ),
                            ft.Container(
                                content=ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_size=20,
                                    bgcolor="#410f5d",
                                    icon_color="white",
                                    tooltip="Trocar foto",
                                    on_click=lambda _: file_picker.pick_files(
                                        allow_multiple=False,
                                        allowed_extensions=["jpg", "jpeg", "png"],
                                    ),
                                ),
                                alignment=alignment.bottom_right,
                            ),
                        ],
                        width=130,
                        height=130,
                    ),
                    
                    ft.Text(
                        value="NOME COMPLETO: PEDRO AFONSO\n"
                            "ENDEREÇO: RUA EXEMPLO, 123, APTO 456\n"
                            "CEP: 35500-000\n"
                            "BAIRRO: CENTRO\n"
                            "CIDADE: SÃO PAULO\n"
                            "FREQUENTA A ACADEMIA: FITMASTER",
                        color="white",
                        size=14,
                        text_align="center",
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )
        page.update()  

    file_picker = ft.FilePicker(on_result=change_profile_image)
    page.overlay.append(file_picker)

   
    show_profile_section()
