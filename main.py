import flet as ft

def main(page: ft.Page):
    # メモ部を生成する関数
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
                        border=ft.InputBorder.NONE,
                        multiline=True      # 複数行入力可能にする
                    ),
                ]
            ),
            padding=ft.padding.symmetric(vertical=5, horizontal=15),
            border=ft.border.all(width=2, color=ft.colors.BLACK54),
            border_radius=20
        )

    # メモを追加する関数
    def add_memo(e):
        memo_column.controls.append(create_new_memo())
        memo_column.update()

    # メモを表示するためのColumn
    memo_column = ft.Column(
        controls=[]
    )

    # メモを追加するためのボタン
    add_button = ft.Row(    # ボタンを横方向に伸ばすために(expandプロパティを使用)、Rowを使用
        controls=[
            ft.FilledTonalButton(
                content=ft.Text(
                    value="メモを追加",
                    size=20
                ),
                height=50,
                expand=1,   # ボタンを横に伸ばす
                on_click=add_memo,
            )
        ]
    )

    page.add(memo_column, add_button)

ft.app(main)
