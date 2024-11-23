from flet import *
import flet as ft

def main(page: Page):
    # Definindo o título da página
    page.title = "Navbar"
    page.window.width = 400
    page.theme_mode = ThemeMode.DARK
    page.scroll = 'auto'
    page.bgcolor = "#2b0a3d"
    page.appbar = AppBar(title=Text('FitMaster'),bgcolor="#61188a")
    

    def click_index(e):
        bt = e.control.selected_index

        if bt == 0:
            page.clean()
            page.add(Text(value='Página 1'), Image(src=f"imagens\gym.jpg"))
            page.bgcolor = "#2b0a3d"
            page.update()

        # se index = 1
        if bt  == 1:
            page.clean()
            page.add(Text(value='Página 2'), Image(src=f""))
            page.bgcolor = "#2b0a3d"
            page.update()

        if bt == 2:
            page.clean()
            page.bgcolor = "#2b0a3d"
            page.update()

    page.navigation_bar = NavigationBar(
            bgcolor="#61188a",
            on_change=click_index,
            destinations=[
                    NavigationDestination(icon=icons.HOME, label='HOME'),
                    NavigationDestination(icon=icons.SHOPPING_BAG, label='LOJA'),
                    NavigationDestination(icon=icons.PERSON, label='PERFIL', )])

    page.add()    

app(target=main)
