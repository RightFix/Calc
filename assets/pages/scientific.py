from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
# from kivy.uix.button import Button
from ..ui_custom import CustomBoxLayout, RoundedButton
import math
Button = RoundedButton

class SciScreen(Screen):
    HEADER_COLOR = (0.3, 0.3, 0.5, 1)
    BG_COLOR = (0.95, 0.95, 0.95, 1)
    NUM_BTN_COLOR = (0.25, 0.25, 0.25, 1)
    OP_BTN_COLOR = (0.9, 0.6, 0.0, 1)
    FUNC_BTN_COLOR = (0.0, 0.5, 0.6, 1)
    NAV_BTN_COLOR = (0.4, 0.4, 0.5, 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_result = ""
        self.current_angle_mode = "deg"
        self.build_ui()

    def build_ui(self):
        main_layout = CustomBoxLayout(
            orientation="vertical", spacing=10, padding=[15, 10, 15, 10],
        )

        app_bar = BoxLayout(size_hint_y=None, height=50, padding=15)
        header = Label(
            text="[b]Scientific[/b]",
            markup=True,
            font_size=26,
            halign="left",
            valign="center",
            color=(1, 1, 1, 1),
            size_hint_x=0.4,
        )
        app_bar.add_widget(header)

        top_nav = BoxLayout(
            size_hint_y=None, height=50, spacing=8, padding=[5, 5, 5, 5]
        )
        calc_btn = Button(
            text="Calc",
            font_size=16,
            background_color=(0.0, 0.5, 0.8, 1),
            color=(1, 1, 1, 1),
            bold=True,
        )
        calc_btn.bind(on_release=lambda x: self.go_to("calculator_screen"))

        assets_btn = Button(
            text="Assets",
            font_size=16,
            background_color=(0.3, 0.6, 0.3, 1),
            color=(1, 1, 1, 1),
            bold=True,
        )
        assets_btn.bind(on_release=lambda x: self.go_to("assets_val_screen"))

        tvm_btn = Button(
            text="TVM",
            font_size=16,
            background_color=(0.15, 0.35, 0.55, 1),
            color=(1, 1, 1, 1),
            bold=True,
        )
        tvm_btn.bind(on_release=lambda x: self.go_to("tvm_screen"))

        sci_btn = Button(
            text="Sci",
            font_size=16,
            background_color=(0.3, 0.3, 0.5, 1),
            color=(1, 1, 1, 1),
            bold=True,
        )
        sci_btn.bind(on_release=lambda x: self.go_to("sci_screen"))

        top_nav.add_widget(calc_btn)
        top_nav.add_widget(assets_btn)
        top_nav.add_widget(tvm_btn)
        top_nav.add_widget(sci_btn)

        main_layout.add_widget(app_bar)
        main_layout.add_widget(top_nav)

        display_container = BoxLayout(
            orientation="vertical", size_hint_y=0.25, padding=[10, 5, 10, 5], spacing=2
        )

        self.result_label = Label(
            text="",
            halign="right",
            font_size=18,
            size_hint_x=1,
            size_hint_y=0.35,
            text_size=(None, None),
            color=(0.3,.3,.3,1),
            padding=[10, 0],
        )
        self.display_label = Label(
            text="0",
            halign="right",
            font_size=42,
            size_hint_x=1,
            size_hint_y=0.65,
            text_size=(None, None),
            color=(0.3,0.3,0.3,1),
            padding=[10, 0],
        )
        self.display_label.bind(
            size=lambda inst, val: setattr(inst, "text_size", (inst.width, None))
        )
        display_container.add_widget(self.result_label)
        display_container.add_widget(self.display_label)
        main_layout.add_widget(display_container)

        functions_row = BoxLayout(
            size_hint_y=None, height=45, spacing=8, padding=[5, 5, 5, 5]
        )
        func_buttons = [
            ("sin", "sin"),
            ("cos", "cos"),
            ("tan", "tan"),
            ("log", "log"),
            ("ln", "ln"),
            ("√", "sqrt"),
            ("^", "pow"),
            ("π", "pi"),
            ("e", "e"),
            ("DEG", "deg"),
        ]
        for text, action in func_buttons:
            btn = Button(
                text=text,
                font_size=16,
                background_color=self.FUNC_BTN_COLOR,
                color=(1, 1, 1, 1),
                bold=True,
            )
            btn.bind(on_release=lambda b, a=action: self.on_func_press(a))
            functions_row.add_widget(btn)
        main_layout.add_widget(functions_row)

        buttons_grid = GridLayout(
            cols=4, rows=5, spacing=8, padding=[5, 10, 5, 5], size_hint_y=0.45
        )
        buttons = [
            ("C", "clear", self.NUM_BTN_COLOR, (0.7, 0.3, 0.3, 1)),
            ("(", "(", self.OP_BTN_COLOR, (1, 1, 1, 1)),
            (")", ")", self.OP_BTN_COLOR, (1, 1, 1, 1)),
            ("Del", "delete", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("7", "7", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("8", "8", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("9", "9", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("÷", "÷", self.OP_BTN_COLOR, (1, 1, 1, 1)),
            ("4", "4", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("5", "5", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("6", "6", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("×", "×", self.OP_BTN_COLOR, (1, 1, 1, 1)),
            ("1", "1", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("2", "2", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("3", "3", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("-", "-", self.OP_BTN_COLOR, (1, 1, 1, 1)),
            ("Ans", "ans", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("0", "0", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            (".", ".", self.NUM_BTN_COLOR, (1, 1, 1, 1)),
            ("=", "calc", self.OP_BTN_COLOR, (1, 1, 1, 1)),
        ]
        for text, action, bg_color, text_color in buttons:
            btn = Button(
                text=text,
                font_size=26,
                background_color=bg_color,
                color=text_color,
                bold=True,
            )
            action_capture = action
            btn.bind(on_release=lambda b, a=action_capture: self.on_button_press(a))
            buttons_grid.add_widget(btn)

        main_layout.add_widget(buttons_grid)

        self.add_widget(main_layout)

    def on_button_press(self, action):
        if action == "clear":
            self.display_label.text = "0"
            self.result_label.text = ""
        elif action == "delete":
            if self.display_label.text and self.display_label.text != "0":
                if self.display_label.text[-5:] == "sqrt(":
                    self.display_label.text = self.display_label.text[:-5]
                elif self.display_label.text[-4:] == "tan(":
                    self.display_label.text = self.display_label.text[:-4]  
                elif self.display_label.text[-4:] == "sin(":
                    self.display_label.text = self.display_label.text[:-4]  
                elif self.display_label.text[-4:] == "cos(":
                    self.display_label.text = self.display_label.text[:-4]  
                elif self.display_label.text[-4:] == "log(":
                    self.display_label.text = self.display_label.text[:-4]  
                else:    
                    self.display_label.text = self.display_label.text[:-1]
            if not self.display_label.text:
                self.display_label.text = "0"
        elif action == "calc":
            self.calculate()
        elif action == "ans":
            if self.last_result:
                if self.display_label.text == "0":
                    self.display_label.text = self.last_result
                else:
                    self.display_label.text += self.last_result
        else:
            if self.display_label.text == "0":
                self.display_label.text = action
            else:
                self.display_label.text += action

    def on_func_press(self, action):
        if action in ("sin", "cos", "tan", "log", "ln"):
            if self.display_label.text == "0":
                self.display_label.text = f"{action}("
            else:
                self.display_label.text += f"{action}("
        elif action == "pow":
            if self.display_label.text == "0":
                self.display_label.text = "^"
            else:
                self.display_label.text += "^"
        elif action == "sqrt":
            if self.display_label.text == "0":
                self.display_label.text = "√"
            else:
                self.display_label.text += "√"
        elif action == "pi":
            if self.display_label.text == "0":
                self.display_label.text = "π"
            else:
                self.display_label.text += "π"
        elif action == "e":
            if self.display_label.text == "0":
                self.display_label.text = str(math.e)
            else:
                self.display_label.text += str(math.e)
        elif action == "deg":
            if self.current_angle_mode == "deg":
                self.current_angle_mode = "rad"
                self.result_label.text = "Mode: RAD"
            else:
                self.current_angle_mode = "deg"
                self.result_label.text = "Mode: DEG"

    def calculate(self, *args):
        try:
            expr = (
                self.display_label.text.replace("×", "*")
                .replace("÷", "/")
                .replace("^", "**")
                .replace("π",str(math.pi))
            )
            if self.current_angle_mode == "deg":
                expr = (
                    expr.replace("sin(", "math.sin(math.radians(")
                    .replace("cos(", "math.cos(math.radians(")
                    .replace("tan(", "math.tan(math.radians(")
                )
            else:
                expr = (
                    expr.replace("sin(", "math.sin(")
                    .replace("cos(", "math.cos(")
                    .replace("tan(", "math.tan(")
                )
            expr = (
                expr.replace("log(", "math.log10(")
                .replace("ln(", "math.log(")
                .replace("√", "math.sqrt(")
            )
            result = eval(expr)
            result = round(result, 10)
            self.last_result = str(result)
            self.display_label.text = str(result)
            self.result_label.text = str(result)
        except (SyntaxError, ZeroDivisionError, ValueError):
            self.result_label.text = "Error"

    def go_to(self, screen_name):
        self.manager.current = screen_name
