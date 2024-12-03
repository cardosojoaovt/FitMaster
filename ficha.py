from flet import *
import flet as ft
import time
from threading import Thread

def TelaFicha(page: ft.Page, navegar_para, *args):
    page.title = "FitMaster - Ficha"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_width = 375
    page.window_height = 667
    page.bgcolor = "#2b0a3d"

    running = False
    time_seconds = 0

    def format_time(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02}:{m:02}:{s:02}"

    timer_text = ft.Text(format_time(time_seconds), size=40, color="white", weight="bold")

    def start_timer(e):
        nonlocal running, time_seconds
        if not running:  
            running = True

            def update_time():
                nonlocal time_seconds
                while running:
                    time.sleep(1)
                    time_seconds += 1
                    timer_text.value = format_time(time_seconds)
                    page.update()

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

    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_color="white",
                    on_click=lambda e: navegar_para("menu"),  
                ),
                ft.Text("Minha Ficha", color="white", size=24, weight="bold"),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.symmetric(vertical=10),
    )

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

    timer = ft.Container(
        content=timer_text,
        alignment=ft.alignment.center,
        padding=ft.padding.all(20),
        border_radius=10,
        bgcolor="#000000",
    )

    timer_controls = ft.Row(
        controls=[
            ft.ElevatedButton(content=ft.Icon(name=ft.icons.PLAY_ARROW, color="purple"), bgcolor="white", on_click=start_timer),
            ft.ElevatedButton(content=ft.Icon(name=ft.icons.PAUSE, color="purple"), bgcolor="white", on_click=pause_timer),
            ft.ElevatedButton(content=ft.Icon(name=ft.icons.RESTART_ALT, color="purple"), bgcolor="white", on_click=reset_timer),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )

    page.add(
        header,
        exercise_list,
        ft.Container(content=timer, padding=10),
        ft.Container(content=timer_controls, padding=10),
    )
