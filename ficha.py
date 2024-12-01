import flet as ft
import time
from threading import Thread

def main(page: ft.Page):
    # Configurações gerais da página
    page.title = "FitMaster - Ficha"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_width = 375
    page.window_height = 667
    page.bgcolor = "#2b0a3d"

    # Variáveis para controlar o cronômetro
    running = False
    time_seconds = 0

    # Função para formatar o tempo (segundos -> HH:MM:SS)
    def format_time(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02}:{m:02}:{s:02}"

    # Atualiza o display do cronômetro
    timer_text = ft.Text(format_time(time_seconds), size=40, color="white", weight="bold")

    # Função que controla o cronômetro
    def start_timer(e):
        nonlocal running, time_seconds
        if not running:  # Evita múltiplas threads
            running = True

            def update_time():
                nonlocal time_seconds
                while running:
                    time.sleep(1)
                    time_seconds += 1
                    timer_text.value = format_time(time_seconds)
                    page.update()

            # Inicia uma thread para atualizar o cronômetro
            Thread(target=update_time, daemon=True).start()

    def pause_timer(e):
        nonlocal running
        running = False

    def reset_timer(e):
        nonlocal running, time_seconds
        running = False
        time_seconds = 0
        timer_text.value = format_time(time_seconds)
        page.update()

    # Cabeçalho
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.Icons.ARROW_BACK, color="white"),
                ft.Text("Minha Ficha", color="white", size=24, weight="bold"),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.symmetric(vertical=10),
    )

    # Lista de exercícios
    exercises = [
        "Pulley Frente    3x - 12 reps",
        "Rosca Direta     3x - 12 reps",
        "Crucifixo        3x - 15 reps",
        "Banco Extensor   3x - 12 reps",
        "Triceps Corda    3x - 10 reps",
    ]

    def create_exercise_item(number, text):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(str(number), size=18, weight="bold", color="white"),
                        width=40,
                        height=40,
                        bgcolor="#5E0080",
                        border_radius=20,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Text(text, size=16, color="black"),
                        padding=ft.padding.only(left=10),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            height=50,
            padding=ft.padding.all(10),
            border=ft.border.all(color="#5E0080", width=2),
            border_radius=10,
            bgcolor="white",
            margin=ft.margin.symmetric(vertical=5),
        )

    exercise_list = ft.Column(
        controls=[
            create_exercise_item(i + 1, exercises[i]) for i in range(len(exercises))
        ]
    )

    # Cronômetro
    timer = ft.Container(
        content=timer_text,
        alignment=ft.alignment.center,
        padding=ft.padding.all(20),
        border_radius=10,
        bgcolor="#000000",
    )

    # Botões do cronômetro
    timer_controls = ft.Row(
        controls=[
            ft.ElevatedButton(content=ft.Icon(name=ft.Icons.PLAY_ARROW, color="purple"),bgcolor="white", on_click=start_timer),
            ft.ElevatedButton(content=ft.Icon(name=ft.Icons.PAUSE, color="purple"),bgcolor="white", on_click=pause_timer),
            ft.ElevatedButton(content=ft.Icon(name=ft.Icons.RESTART_ALT, color="purple"),bgcolor="white", on_click=reset_timer),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )

    # Montando a página
    page.add(
        header,
        exercise_list,
        ft.Container(content=timer, padding=10),
        ft.Container(content=timer_controls, padding=10),
    )

ft.app(target=main)
