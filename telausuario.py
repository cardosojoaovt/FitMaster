from flet import *
import flet as ft

def main(page: ft.Page):
    # Configurações gerais da página
    page.title = "FitMaster - Perfil"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window.width = 375
    page.window.height = 667
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centraliza o conteúdo verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centraliza o conteúdo horizontalmente
    page.bgcolor = "#2b0a3d"
    page.scroll = 'auto'
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
        page.clean()  # Limpa a página antes de adicionar o novo conteúdo
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
                                "CEP: 35500-000\n"
                                "BAIRRO: CENTRO\n"
                                "CIDADE: SÃO PAULO\n"
                                "FREQUENTA A ACADEMIA: FITMASTER",
                            color="white",
                            size=14,
                            text_align="center",
                            
                        ),
                        # Calendário horizontal com dias da semana
                        Divider(height=30, color=ft.colors.GREY),
                        Row(
                            [
                                # Dias da semana (siglas)
                                Container(content=Text("Seg", color="white", size=14), alignment=alignment.center),
                                Container(content=Text("Ter", color="white", size=14), alignment=alignment.center),
                                Container(content=Text("Qua", color="white", size=14), alignment=alignment.center),
                                Container(content=Text("Qui", color="white", size=14), alignment=alignment.center),
                                Container(content=Text("Sex", color="white", size=14), alignment=alignment.center),
                                Container(content=Text("Sáb", color="white", size=14), alignment=alignment.center),
                                Container(content=Text("Dom", color="white", size=14), alignment=alignment.center),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,  # Alinha todos os itens no centro
                            spacing=10,  # Espaço entre os dias
                        ),
                        # Indicadores de presença (círculos coloridos)
                        Row(
                            [
                                # Presença nos dias da semana, representada por círculos coloridos
                                Container(
                                    content=CircleAvatar(color=ft.colors.GREEN),  # Presença
                                    width=30,
                                    height=30,
                                    alignment=alignment.center,
                                ),
                                Container(
                                    content=CircleAvatar(color=ft.colors.RED),  # Ausente
                                    width=30,
                                    height=30,
                                    alignment=alignment.center,
                                ),
                                Container(
                                    content=CircleAvatar(color=ft.colors.GREEN),  # Presença
                                    width=30,
                                    height=30,
                                    alignment=alignment.center,
                                ),
                                Container(
                                    content=CircleAvatar(color=ft.colors.RED),  # Ausente
                                    width=30,
                                    height=30,
                                    alignment=alignment.center,
                                ),
                                Container(
                                    content=CircleAvatar(color=ft.colors.GREEN),  # Presença
                                    width=30,
                                    height=30,
                                    alignment=alignment.center,
                                ),
                                Container(
                                    content=CircleAvatar(color=ft.colors.RED),  # Ausente
                                    width=30,
                                    height=30,
                                    alignment=alignment.center,
                                ),
                                Container(
                                    content=CircleAvatar(color=ft.colors.GREEN),  # Presença
                                    width=30,
                                    height=30,
                                    alignment=alignment.center,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os círculos
                            spacing=10,  # Espaçamento entre os círculos
                        ),
                    ],
                    alignment="center",  # Centraliza todos os itens na coluna
                    horizontal_alignment="center",  # Centraliza horizontalmente
                    spacing=20,  # Espaçamento entre os componentes
                ),
                alignment=alignment.center,
                expand=True,  # Expande o container para ocupar toda a tela
                padding=20,
            )
        )
        page.bgcolor = "#2b0a3d"  # Cor de fundo do aplicativo
        page.update()

    # FilePicker para selecionar a foto
    file_picker = FilePicker(on_result=change_profile_image)
    page.overlay.append(file_picker)

    # Exibe a seção de perfil logo ao iniciar
    show_profile_section()

app(target=main)
