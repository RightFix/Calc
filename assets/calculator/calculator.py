from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle


class CalculatorScreen(Screen):
    last_result = ""
    BTN_COLOR = (0.2, 0.2, 0.2, 1)
    BTN_TEXT_COLOR = (1, 1, 1, 1)
    OP_BTN_COLOR = (0.3, 0.3, 0.3, 1)
    NUM_BTN_COLOR = (0.15, 0.15, 0.15, 1)
    CALC_BTN_COLOR = (0.0, 0.6, 0.8, 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        with self.canvas.before:
            Color(0.1, 0.1, 0.1, 1)
            self.bg = RoundedRectangle(size=self.size, pos=self.pos)

        main_layout = BoxLayout(orientation="vertical", spacing=8, padding=10)

        app_bar = BoxLayout(
            size_hint_y=None,
            height=60,
            padding=[15, 10],
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        app_title = Label(
            text="Calculator",
            font_size=28,
            halign="left",
            valign="middle",
            color=(1, 1, 1, 1),
            bold=True,
        )
        app_bar.add_widget(app_title)
        main_layout.add_widget(app_bar)

        display_container = BoxLayout(
            orientation="vertical",
            size_hint_y=0.25,
            padding=[15, 5, 15, 10],
            spacing=5,
        )

        self.result_label = TextInput(
            text="",
            font_size=18,
            halign="right",
            # valign="bottom",
            readonly=True,
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(0.7, 0.7, 0.7, 1),
            cursor_color=(1, 1, 1, 0),
            multiline=False,
            size_hint_y=0.4,
            border=[0, 0, 0, 0],
        )
        self.display_label = TextInput(
            text="",
            font_size=48,
            halign="right",
            # valign="bottom",
            readonly=True,
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 0),
            multiline=False,
            size_hint_y=0.6,
            border=[0, 0, 0, 0],
            padding=[0, 5, 0, 5],
        )
        display_container.add_widget(self.result_label)
        display_container.add_widget(self.display_label)
        main_layout.add_widget(display_container)

        buttons_grid = GridLayout(cols=4, rows=5, spacing=8, padding=[5, 5, 5, 5])
        buttons_layout = [
            ("C", "clear", self.BTN_COLOR),
            ("÷", "÷", self.OP_BTN_COLOR),
            ("×", "×", self.OP_BTN_COLOR),
            ("⌫", "delete", self.OP_BTN_COLOR),
            ("7", "7", self.NUM_BTN_COLOR),
            ("8", "8", self.NUM_BTN_COLOR),
            ("9", "9", self.NUM_BTN_COLOR),
            ("-", "-", self.OP_BTN_COLOR),
            ("4", "4", self.NUM_BTN_COLOR),
            ("5", "5", self.NUM_BTN_COLOR),
            ("6", "6", self.NUM_BTN_COLOR),
            ("+", "+", self.OP_BTN_COLOR),
            ("1", "1", self.NUM_BTN_COLOR),
            ("2", "2", self.NUM_BTN_COLOR),
            ("3", "3", self.NUM_BTN_COLOR),
            ("=", "calc", self.CALC_BTN_COLOR),
            ("%", "percent", self.BTN_COLOR),
            ("0", "0", self.NUM_BTN_COLOR),
            (".", ".", self.NUM_BTN_COLOR),
            ("Ans", "ans", self.BTN_COLOR),
        ]

        for text, action, color in buttons_layout:
            btn = Button(
                text=text,
                font_size=28,
                background_color=(0, 0, 0, 0),
                color=color,
                bold=True,
            )
            with btn.canvas.before:
                Color(*color)
                RoundedRectangle(
                    size=btn.size,
                    pos=btn.pos,
                    radius=[15, 15, 15, 15],
                )
            action_capture = action
            btn.bind(
                on_press=lambda btn: setattr(btn, "opacity", 0.7),
            )
            btn.bind(
                on_release=lambda btn, a=action_capture: self.on_button_press(a),
            )
            buttons_grid.add_widget(btn)

        main_layout.add_widget(buttons_grid)

        nav_layout = BoxLayout(size_hint_y=None, height=60, spacing=10, padding=10)
        tvm_btn = Button(
            text="TVM",
            font_size=18,
            background_color=(0, 0.5, 0.7, 1),
            color=(1, 1, 1, 1),
            bold=True,
        )
        tvm_btn.bind(on_release=lambda x: self.go_to("tvm_screen"))
        assets_btn = Button(
            text="Assets",
            font_size=18,
            background_color=(0, 0.5, 0.7, 1),
            color=(1, 1, 1, 1),
            bold=True,
        )
        assets_btn.bind(on_release=lambda x: self.go_to("assets_val_screen"))
        nav_layout.add_widget(tvm_btn)
        nav_layout.add_widget(assets_btn)
        main_layout.add_widget(nav_layout)

        self.add_widget(main_layout)

    def on_button_press(self, action):
        if action == "clear":
            self.clear_display()
        elif action == "delete":
            self.delete_last()
        elif action == "calc":
            self.calculate()
        elif action == "percent":
            self.percentage()
        elif action == "ans":
            self.use_answer()
        else:
            self.append_text(action)

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
