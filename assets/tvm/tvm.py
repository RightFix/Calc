from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math


class TVMScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        main_layout = BoxLayout(orientation="vertical", spacing=5, padding=5)

        app_bar = BoxLayout(size_hint_y=None, height=50, padding=10)
        app_bar.add_widget(Label(text="TVM Calculator", font_size=20, halign="left"))
        main_layout.add_widget(app_bar)

        inputs_layout = GridLayout(cols=2, size_hint_y=0.5, padding=10, spacing=10)
        inputs_layout.add_widget(Label(text="Present Value (PV):", halign="right"))
        self.pv_input = TextInput(hint_text="0", multiline=False, input_filter="float")
        inputs_layout.add_widget(self.pv_input)

        inputs_layout.add_widget(Label(text="Future Value (FV):", halign="right"))
        self.fv_input = TextInput(hint_text="0", multiline=False, input_filter="float")
        inputs_layout.add_widget(self.fv_input)

        inputs_layout.add_widget(Label(text="Rate (%):", halign="right"))
        self.rate_input = TextInput(
            hint_text="0", multiline=False, input_filter="float"
        )
        inputs_layout.add_widget(self.rate_input)

        inputs_layout.add_widget(Label(text="Periods:", halign="right"))
        self.periods_input = TextInput(
            hint_text="0", multiline=False, input_filter="float"
        )
        inputs_layout.add_widget(self.periods_input)

        main_layout.add_widget(inputs_layout)

        buttons_layout = GridLayout(
            cols=2, rows=3, size_hint_y=0.3, padding=5, spacing=10
        )
        buttons_layout.add_widget(
            Button(text="Future Value", on_press=self.calculate_future_value)
        )
        buttons_layout.add_widget(
            Button(text="Present Value", on_press=self.calculate_present_value)
        )
        buttons_layout.add_widget(
            Button(text="Payment (PMT)", on_press=self.calculate_pmt)
        )
        buttons_layout.add_widget(
            Button(text="Periods (NPER)", on_press=self.calculate_nper)
        )
        buttons_layout.add_widget(Button(text="Clear", on_press=self.clear_inputs))
        buttons_layout.add_widget(
            Button(text="Exit", on_press=lambda x: self.go_to("calculator_screen"))
        )
        main_layout.add_widget(buttons_layout)

        self.result_label = Label(text="Result: ", font_size=18, size_hint_y=0.2)
        main_layout.add_widget(self.result_label)

        self.add_widget(main_layout)

    def calculate_future_value(self, *args):
        try:
            p = float(self.pv_input.text or 0)
            r = float(self.rate_input.text or 0) / 100
            n = float(self.periods_input.text or 0)
            if r == 0:
                fv = p
            else:
                fv = p * ((1 + r) ** n)
            self.result_label.text = f"Future Value: {fv:,.2f}"
        except (ValueError, ZeroDivisionError):
            self.result_label.text = "Error: Enter valid numbers"

    def calculate_present_value(self, *args):
        try:
            fv = float(self.fv_input.text or 0)
            r = float(self.rate_input.text or 0) / 100
            n = float(self.periods_input.text or 0)
            if r == 0:
                pv = fv
            else:
                pv = fv / ((1 + r) ** n)
            self.result_label.text = f"Present Value: {pv:,.2f}"
        except (ValueError, ZeroDivisionError):
            self.result_label.text = "Error: Enter valid numbers"

    def calculate_pmt(self, *args):
        try:
            pv = float(self.pv_input.text or 0)
            r = float(self.rate_input.text or 0) / 100
            n = float(self.periods_input.text or 0)
            if r == 0:
                pmt = pv / n if n > 0 else 0
            else:
                pmt = (pv * r * (1 + r) ** n) / ((1 + r) ** n - 1)
            self.result_label.text = f"Payment: {pmt:,.2f} per period"
        except (ValueError, ZeroDivisionError):
            self.result_label.text = "Error: Enter valid numbers"

    def calculate_nper(self, *args):
        try:
            pv = float(self.pv_input.text or 0)
            fv = float(self.fv_input.text or 0)
            r = float(self.rate_input.text or 0) / 100
            if r == 0:
                n = -fv / pv if pv != 0 else 0
            else:
                n = math.log(fv / pv) / math.log(1 + r) if pv > 0 and fv > 0 else 0
            self.result_label.text = f"Periods: {n:,.2f}"
        except (ValueError, ZeroDivisionError):
            self.result_label.text = "Error: Enter valid numbers"

    def clear_inputs(self, *args):
        self.pv_input.text = ""
        self.fv_input.text = ""
        self.rate_input.text = ""
        self.periods_input.text = ""
        self.result_label.text = "Result: "

    def go_to(self, screen_name):
        self.manager.current = screen_name
