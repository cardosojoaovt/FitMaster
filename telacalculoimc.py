from flet import *
import flet as ft

def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "FitMaster - Menu"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window.width = 375
    page.window.height = 667
    page.bgcolor = "#2b0a3d"
    page.scroll = 'auto'
    page.appbar = AppBar(bgcolor="#410f5d")

    # Função para calcular o IMC e atualizar o gráfico
    def calcular_imc(e):
        try:
            # Obter dados do usuário
            peso = float(input_peso.value)
            altura = float(input_altura.value) / 100  # Converter altura para metros
            imc = peso / (altura ** 2)

            # Atualizar o texto do resultado do IMC
            resultado_texto.value = f"IMC: {imc:.1f}"

            # Determinar faixa do IMC e situação
            if imc < 18.5:
                situacao_texto.value = "Abaixo do Peso"
                situacao_texto.color = ft.colors.BLUE
                gauge_color = ft.colors.BLUE
            elif 18.5 <= imc < 25:
                situacao_texto.value = "Saudável"
                situacao_texto.color = ft.colors.GREEN
                gauge_color = ft.colors.GREEN
            elif 25 <= imc < 30:
                situacao_texto.value = "Sobrepeso"
                situacao_texto.color = ft.colors.ORANGE
                gauge_color = ft.colors.ORANGE
            else:
                situacao_texto.value = "Obesidade"
                situacao_texto.color = ft.colors.RED
                gauge_color = ft.colors.RED

            # Atualizar o velocímetro
            gauge_bar.value = min(imc / 40, 1)  # Escala de 0 a 1
            gauge_bar.color = gauge_color

            # Atualizar a página
            page.update()
        except ValueError:
            resultado_texto.value = "Valores inválidos. Insira números!"
            page.update()

    # Entradas do usuário
    input_peso = ft.TextField(label="Peso (kg)", width=150, text_align=ft.TextAlign.CENTER)
    input_altura = ft.TextField(label="Altura (cm)", width=150, text_align=ft.TextAlign.CENTER)

    # Botão de cálculo
    btn_calcular = ft.ElevatedButton(
        text="Calcular IMC",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=calcular_imc,
    )

    # Texto para exibir o IMC
    resultado_texto = ft.Text(value="IMC: --", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)

    # Situação do IMC
    situacao_texto = ft.Text(value="Situação: --", size=20, color=ft.colors.GREY)

    # Velocímetro com barra de progresso circular
    gauge_bar = ft.ProgressRing(
        value=0,
        width=200,
        height=200,
        stroke_width=15,
        color=ft.colors.GREY,
    )

    # Layout centralizado
    page.add(
        ft.Column(  # Usando Column para centralizar
            [
                ft.Text("Calculadora de IMC", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Divider(height=20, color=ft.colors.GREY),
                ft.Row([input_peso, input_altura], alignment=ft.MainAxisAlignment.CENTER),
                btn_calcular,
                ft.Divider(height=20, color=ft.colors.GREY),
                ft.Column(
                    [
                        resultado_texto,
                        gauge_bar,
                        situacao_texto,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Garantindo a centralização da coluna principal
            spacing=20,
        )
    )

# Rodar o aplicativo
ft.app(target=main)
