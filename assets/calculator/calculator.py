from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button



class CalculatorScreen(Screen):
    last_result = ""
    BG_COLOR = (0.95, 0.95, 0.95, 1)
    HEADER_COLOR = (0.2, 0.2, 0.3, 1)
    NUM_BTN_COLOR = (0.25, 0.25, 0.25, 1)
    OP_BTN_COLOR = (0.9, 0.6, 0.0, 1)
    CALC_BTN_COLOR = (0.0, 0.5, 0.8, 1)
    NAV_BTN_COLOR = (0.4, 0.4, 0.5, 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        main_layout = BoxLayout(
            orientation="vertical", spacing=10, padding=[15, 10, 15, 10]
        )

        app_bar = BoxLayout(size_hint_y=None, height=65, padding=15)
        header = Label(
            text="[b]Calculator[/b]",
            markup=True,
            font_size=28,
            halign="left",
            valign="center",
            color=(1, 1, 1, 1),
        )
        app_bar.add_widget(header)
        # with app_bar.canvas.before:
        #     Color(*self.HEADER_COLOR)
        #     RoundedRectangle(size=app_bar.size, pos=app_bar.pos, radius=[15, 15, 0, 0])
        # main_layout.add_widget(app_bar)

        display_container = BoxLayout(
            orientation="vertical", size_hint_y=0.40, padding=[10, 5, 10, 5], spacing=2
        )

        self.result_label = Label(
            text="",
            halign="right",
            font_size=18,
            size_hint_x=1,
            size_hint_y=0.35,
            text_size=(None, None),
            color=(1, 1, 1, 1),
            padding=[10, 0],
        )
        self.display_label = Label(
            text="0",
            halign="right",
            font_size=52,
            size_hint_x=1,
            size_hint_y=0.65,
            text_size=(None, None),
            color=(1, 1, 1, 1),
            padding=[10, 0],
        )
        self.result_label.bind(
            size=lambda inst, val: setattr(inst, "text_size", (inst.width, None))
        )
        self.display_label.bind(
            size=lambda inst, val: setattr(inst, "text_size", (inst.width, None))
        )
        display_container.add_widget(self.result_label)
        display_container.add_widget(self.display_label)
        main_layout.add_widget(display_container)

        buttons_grid = GridLayout(
            cols=4, rows=5, spacing=8, padding=[5, 10, 5, 5], size_hint_y=0.40
        )
        buttons = [
            ("C", "clear", self.NUM_BTN_COLOR, (0.7, 0.3, 0.3, 1)),
            ("÷", "÷", self.OP_BTN_COLOR, (1, 1, 1, 1)),
            ("×", "×", self.OP_BTN_COLOR, (1, 1, 1, 1)),
            ("⌫", "delete", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("7", "7", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("8", "8", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("9", "9", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("-", "-", self.OP_BTN_COLOR, (1, 1, 1, 1)),
            ("4", "4", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("5", "5", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("6", "6", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("+", "+", self.OP_BTN_COLOR, (1, 1, 1, 1)),
            ("1", "1", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("2", "2", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("3", "3", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("=", "calc", self.CALC_BTN_COLOR, (1, 1, 1, 1)),
            ("%", "percent", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("0", "0", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            (".", ".", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("Ans", "ans", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
        ]
        for text, action, bg_color, text_color in buttons:
            btn = Button(
                text=text,
                font_size=28,
                background_color=bg_color,
                color=text_color,
                bold=True,
            )
            action_capture = action
            btn.bind(on_release=lambda btn, a=action_capture: self.on_button_press(a))
            buttons_grid.add_widget(btn)

        main_layout.add_widget(buttons_grid)

        nav_layout = BoxLayout(
            size_hint_y=None, height=55, spacing=12, padding=[5, 10, 5, 5]
        )
        tvm_btn = Button(
            text="TVM",
            font_size=18,
            background_color=self.NAV_BTN_COLOR,
            color=(1, 1, 1, 1),
            bold=True,
        )
        tvm_btn.bind(on_release=lambda x: self.go_to("tvm_screen"))

        assets_btn = Button(
            text="Assets",
            font_size=18,
            background_color=self.NAV_BTN_COLOR,
            color=(1, 1, 1, 1),
            bold=True,
        )
        assets_btn.bind(on_release=lambda x: self.go_to("assets_val_screen"))

        nav_layout.add_widget(tvm_btn)
        nav_layout.add_widget(assets_btn)
        main_layout.add_widget(nav_layout)

        # with main_layout.canvas.before:
        #     Color(*self.BG_COLOR)
        #     RoundedRectangle(
        #         size=main_layout.size, pos=main_layout.pos, radius=[15, 15, 15, 15]
        #     )

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
            if self.display_label.text == "0":
                self.display_label.text = action
            else:
                self.display_label.text += action

    def clear_display(self, *args):
        self.display_label.text = "0"
        self.result_label.text = ""

    def delete_last(self, *args):
        if self.display_label.text and self.display_label.text != "0":
            self.display_label.text = self.display_label.text[:-1]
        if not self.display_label.text:
            self.display_label.text = "0"

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
            if self.display_label.text == "0":
                self.display_label.text = self.last_result
            else:
                self.display_label.text += self.last_result

    def go_to(self, screen_name):
        self.manager.current = screen_name
