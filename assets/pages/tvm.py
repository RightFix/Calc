from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
# from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from ..ui_custom import CustomBoxLayout, RoundedTextInput, RoundedButton
import math

Button = RoundedButton

class TVMScreen(Screen):
    HEADER_COLOR = (0.15, 0.35, 0.55, 1)
    BG_COLOR = (0.95, 0.95, 0.95, 1)
    BTN_COLOR = (0.2, 0.5, 0.7, 1)
    INPUT_BG = (0.85, 0.85, 0.85, 1)
    NAV_BTN_COLOR = (0.4, 0.4, 0.5, 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        main_layout = CustomBoxLayout(
            orientation="vertical", spacing=10, padding=[15, 10, 15, 10], bg_color=(1,1,1,1)
        )

        app_bar = BoxLayout(size_hint_y=None, height=50, padding=15)
        header = Label(
            text="[b]TVM Calculator[/b]",
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
            background_color=self.BTN_COLOR,
            color=(1, 1, 1, 1),
            bold=True,
        )
        tvm_btn.bind(on_release=lambda x: self.go_to("tvm_screen"))

        top_nav.add_widget(calc_btn)
        top_nav.add_widget(assets_btn)
        top_nav.add_widget(tvm_btn)

        main_layout.add_widget(app_bar)
        main_layout.add_widget(top_nav)

        inputs_layout = BoxLayout(
            orientation="vertical", size_hint_y=0.40, spacing=15, padding=10
        )

        inputs_config = [
            ("Present Value (PV):", "0"),
            ("Future Value (FV):", "0"),
            ("Rate (%):", "0"),
            ("Periods:", "0"),
        ]

        for label_text, hint in inputs_config:
            row = BoxLayout(size_hint_y=1, spacing=10)
            lbl = Label(
                text=label_text,
                halign="right",
                valign="center",
                font_size=16,
                size_hint_x=0.35,
                color=(0.2, 0.2, 0.2, 1),
            )
            inp = TextInput(
                hint_text=hint,
                multiline=False,
                input_filter="float",
                font_size=18,
                halign="left",
                padding=[15, 10, 10, 10],
                background_color=self.INPUT_BG,
                foreground_color=(0.2, 0.2, 0.2, 1),
                cursor_color=(0.2, 0.5, 0.8, 1),
                size_hint_x=0.65,
            )
            row.add_widget(lbl)
            row.add_widget(inp)
            inputs_layout.add_widget(row)
            if label_text == "Present Value (PV):":
                self.pv_input = inp
            elif label_text == "Future Value (FV):":
                self.fv_input = inp
            elif label_text == "Rate (%):":
                self.rate_input = inp
            else:
                self.periods_input = inp

        main_layout.add_widget(inputs_layout)

        buttons_layout = GridLayout(
            cols=2, rows=3, size_hint_y=0.30, padding=10, spacing=12
        )
        buttons_config = [
            ("Future Value", self.calculate_future_value),
            ("Present Value", self.calculate_present_value),
            ("Payment (PMT)", self.calculate_pmt),
            ("Periods (NPER)", self.calculate_nper),
            ("Clear", self.clear_inputs),
        ]

        for text, callback in buttons_config:
            btn = Button(
                text=text,
                font_size=18,
                background_color=self.BTN_COLOR,
                color=(1, 1, 1, 1),
                bold=True,
            )
            btn.bind(on_release=callback)
            buttons_layout.add_widget(btn)

        main_layout.add_widget(buttons_layout)

        self.result_label = Label(
            text="Enter values and select calculation",
            font_size=16,
            size_hint_y=0.15,
            halign="center",
            color=(0.2, 0.2, 0.2, 1),
        )
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
        self.result_label.text = "Enter values and select calculation"

    def go_to(self, screen_name):
        self.manager.current = screen_name
