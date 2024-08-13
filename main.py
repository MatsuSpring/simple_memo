import flet as ft

def main(page: ft.Page):
    def create_new_memo():
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.TextField(
                        hint_text="タイトル",
                        hint_style=ft.TextStyle(color=ft.colors.BLACK26),
                        text_size=20,
                        border=ft.InputBorder.UNDERLINE
                    ),
                    ft.TextField(
                        hint_text="ここにメモを入力",
                        hint_style=ft.TextStyle(color=ft.colors.BLACK26),
                        text_size=17,
                        border=ft.InputBorder.NONE
                    ),
                ]
            ),
            padding=ft.padding.symmetric(vertical=5, horizontal=15),
            border=ft.border.all(width=2, color=ft.colors.BLACK54),
            border_radius=20
        )

    memo_column = ft.Column(
        controls=[create_new_memo(), create_new_memo(), create_new_memo()]
    )

    page.add(memo_column)

ft.app(main)
