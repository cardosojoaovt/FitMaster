from flet import *
import flet as ft

def main(page: ft.Page):
    # Configurações gerais da página
    page.title = "Navbar"
    page.window.width = 400
    page.theme_mode = ThemeMode.DARK
    page.scroll = 'auto'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centraliza o conteúdo verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centraliza o conteúdo horizontalmente
    page.bgcolor = "#2b0a3d"
    page.appbar = AppBar(bgcolor="#410f5d")

    # Caminho inicial da imagem de perfil (foto padrão)
    profile_image = "imagens/usuario.png"  # Substitua pelo caminho correto da imagem padrão

    # Função para trocar a foto de perfil
    def change_profile_image(e):
        if file_picker.result and file_picker.result.files:
            new_image = file_picker.result.files[0].path
            nonlocal profile_image
            profile_image = new_image
            show_profile_section()

    # Função para exibir a seção de perfil
    def show_profile_section():
        page.clean()
        page.add(
            Container(
                content=Column(
                    [
                        # Contêiner com a imagem de perfil e o botão de edição
                        Stack(
                            [
                                # Imagem de perfil
                                Container(
                                    content=Image(
                                        src=profile_image,
                                        width=120,
                                        height=120,
                                        fit="cover",
                                        border_radius=60,  # Tornar circular
                                    ),
                                    padding=10,
                                    alignment=alignment.center,
                                ),
                                # Botão de troca de imagem no canto inferior direito da imagem
                                Container(
                                    content=IconButton(
                                        icon=icons.EDIT,
                                        icon_size=20,
                                        bgcolor="#410f5d",
                                        icon_color="white",
                                        tooltip="Trocar foto",
                                        on_click=lambda _: file_picker.pick_files(
                                            allow_multiple=False,  # Apenas uma imagem
                                            allowed_extensions=["jpg", "jpeg", "png"],  # Tipos de arquivo
                                        ),
                                    ),
                                    alignment=alignment.bottom_right,
                                ),
                            ],
                            width=130,
                            height=130,
                        ),
                        # Informações do perfil
                        Text(
                            value="NOME COMPLETO: PEDRO AFONSO\n"
                                "ENDEREÇO: RUA EXEMPLO, 123, APTO 456\n"
                                "CEP: 35500-000"
                                "BAIRRO: CENTRO\n"
                                "CIDADE: SÃO PAULO\n"
                                "FREQUENTA A ACADEMIA: FITMASTER",
                            color="white",
                            size=14,
                            text_align="center",
                        ),
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                ),
                alignment=alignment.center,
                expand=True,
            )
        )
        page.bgcolor = "#2b0a3d"
        page.update()

    # Navegação
    def click_index(e):
        if e.control.selected_index == 2:  # Seção Perfil
            show_profile_section()

    # FilePicker para selecionar a foto
    file_picker = FilePicker(on_result=change_profile_image)
    page.overlay.append(file_picker)

    page.navigation_bar = NavigationBar(
        bgcolor="#410f5d",
        on_change=click_index,
        destinations=[
            NavigationDestination(icon=icons.HOME, label='HOME'),
            NavigationDestination(icon=icons.SHOPPING_BAG, label='LOJA'),
            NavigationDestination(icon=icons.PERSON, label='PERFIL'),
        ]
    )

    page.add()

app(target=main)