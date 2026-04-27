from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class CalculatorScreen(Screen):
    last_result = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        main_layout = BoxLayout(orientation="vertical", spacing=5, padding=5)

        app_bar = BoxLayout(size_hint_y=None, height=50, padding=10)
        app_bar.add_widget(Label(text="Calculator", font_size=20, halign="left"))
        main_layout.add_widget(app_bar)

        display_layout = BoxLayout(orientation="vertical", size_hint_y=0.3, padding=10)

        self.result_label = Label(
            text="", halign="right", valign="middle", font_size=20, size_hint_y=0.3
        )
        self.display_label = Label(
            text="", halign="right", valign="middle", font_size=40
        )
        display_layout.add_widget(self.result_label)
        display_layout.add_widget(self.display_label)

        main_layout.add_widget(display_layout)

        buttons_grid = GridLayout(cols=4, rows=5, spacing=6, size_hint_y=2)
        buttons = [
            ("C", self.clear_display),
            ("÷", lambda: self.append_text("÷")),
            ("×", lambda: self.append_text("×")),
            ("⌫", self.delete_last),
            ("7", lambda: self.append_text("7")),
            ("8", lambda: self.append_text("8")),
            ("9", lambda: self.append_text("9")),
            ("-", lambda: self.append_text("-")),
            ("4", lambda: self.append_text("4")),
            ("5", lambda: self.append_text("5")),
            ("6", lambda: self.append_text("6")),
            ("+", lambda: self.append_text("+")),
            ("1", lambda: self.append_text("1")),
            ("2", lambda: self.append_text("2")),
            ("3", lambda: self.append_text("3")),
            ("=", self.calculate),
            ("%", self.percentage),
            ("0", lambda: self.append_text("0")),
            (".", lambda: self.append_text(".")),
            ("Ans", self.use_answer),
        ]
        for text, callback in buttons:
            btn = Button(text=text, font_size=22, on_press=callback)
            buttons_grid.add_widget(btn)

        main_layout.add_widget(buttons_grid)

        nav_layout = BoxLayout(size_hint_y=None, height=50, spacing=8, padding=5)
        tvm_btn = Button(text="TVM", on_press=lambda x: self.go_to("tvm_screen"))
        assets_btn = Button(
            text="Assets", on_press=lambda x: self.go_to("assets_val_screen")
        )
        nav_layout.add_widget(tvm_btn)
        nav_layout.add_widget(assets_btn)
        main_layout.add_widget(nav_layout)

        self.add_widget(main_layout)

    def append_text(self, text):
        self.display_label.text += text

    def clear_display(self, *args):
        self.display_label.text = ""
        self.result_label.text = ""

    def delete_last(self, *args):
        if self.display_label.text:
            self.display_label.text = self.display_label.text[:-1]

    def calculate(self, *args):
        try:
            expr = self.display_label.text.replace("×", "*").replace("÷", "/")
            result = eval(expr)
            result = round(result, 10)
            self.last_result = str(result)
            self.display_label.text = str(result)
            self.result_label.text = str(result)
        except (SyntaxError, ZeroDivisionError, ValueError):
            self.result_label.text = "Error"

    def percentage(self, *args):
        try:
            if self.display_label.text:
                value = float(self.display_label.text)
                self.display_label.text = str(value * 0.01)
        except ValueError:
            self.result_label.text = "Error"

    def use_answer(self, *args):
        if self.last_result:
            self.display_label.text += self.last_result

    def go_to(self, screen_name):
        self.manager.current = screen_name
