import flet as ft
from login import TelaLogin
from menu import TelaMenu
from ficha import TelaFicha 
from plano import TelaPlano
from usuario import TelaUsuario

def main(page: ft.Page):
    page.title = "FitMaster App"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#2b0a3d"
    page.padding = 20
    page.window_width = 375
    page.window_height = 667

    def navegar_para(tela, *args):
        page.controls.clear()
        if tela == "login":
            TelaLogin(page, navegar_para)
        elif tela == "menu":
            TelaMenu(page, navegar_para, *args)
        elif tela == "ficha_treino":
            TelaFicha(page, navegar_para, *args)
        elif tela == "plano":
            TelaPlano(page, navegar_para, *args)
        elif tela == "usuario":
            TelaUsuario(page, navegar_para, *args)
        page.update()

    navegar_para("login")

ft.app(target=main)
