from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel

Builder.load_file("assets/calculator/calculator.kv")


class Calculator(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def append_text(self, text):
        self.ids.display.text += text

    def clear_display(self):
        self.ids.display.text = ""
        self.ids.result.text = ""

    def delete_last(self):
        if self.ids.display.text:
            self.ids.display.text = self.ids.display.text[:-1]

    def calculate(self):
        try:
            expr = self.ids.display.text.replace("×", "*").replace("÷", "/")
            result = eval(expr)
            result = round(result, 10)
            self.ids.display.text = str(result)
            self.ids.result.text = str(result)
        except (SyntaxError, ZeroDivisionError, ValueError):
            self.ids.result.text = "Error"

    def percentage(self):
        try:
            if self.ids.display.text:
                value = float(self.ids.display.text)
                self.ids.display.text = str(value * 0.01)
        except ValueError:
            self.ids.result.text = "Error"

    def use_answer(self):
        if self.ids.result.text and self.ids.result.text != "Error":
            self.ids.display.text += self.ids.result.text

    def navigate_to(self, screen_name):
        self.manager.app.screen_history.append(screen_name)
        self.manager.current = screen_name
