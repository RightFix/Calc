from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel

Builder.load_file("assets/tvm/tvm.kv")


class TVM(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def calculate_future_value(self):
        try:
            p = float(self.ids.principal.text or 0)
            r = float(self.ids.rate.text or 0) / 100
            n = float(self.ids.periods.text or 0)
            fv = p * ((1 + r) ** n)
            self.ids.result.text = f"Future Value: {fv:,.2f}"
        except ValueError:
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_present_value(self):
        try:
            fv = float(self.ids.fv_input.text or 0)
            r = float(self.ids.rate.text or 0) / 100
            n = float(self.ids.periods.text or 0)
            pv = fv / ((1 + r) ** n)
            self.ids.result.text = f"Present Value: {pv:,.2f}"
        except ValueError:
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_pmt(self):
        try:
            pv = float(self.ids.principal.text or 0)
            r = float(self.ids.rate.text or 0) / 100
            n = float(self.ids.periods.text or 0)
            if r == 0:
                pmt = pv / n
            else:
                pmt = (pv * r * (1 + r) ** n) / ((1 + r) ** n - 1)
            self.ids.result.text = f"Payment: {pmt:,.2f}"
        except ValueError:
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_nper(self):
        try:
            pv = float(self.ids.principal.text or 0)
            fv = float(self.ids.fv_input.text or 0)
            r = float(self.ids.rate.text or 0) / 100
            if r == 0:
                n = -fv / pv if pv != 0 else 0
            else:
                import math
                n = math.log(fv / pv) / math.log(1 + r)
            self.ids.result.text = f"Periods: {n:,.2f}"
        except ValueError:
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_rate(self):
        try:
            pv = float(self.ids.principal.text or 0)
            fv = float(self.ids.fv_input.text or 0)
            n = float(self.ids.periods.text or 0)
            if n == 0 or pv == 0:
                self.ids.result.text = "Error: Invalid values"
                return
            import math
            r = (fv / pv) ** (1 / n) - 1
            self.ids.result.text = f"Rate: {r * 100:,.2f}%"
        except ValueError:
            self.ids.result.text = "Error: Enter valid numbers"

    def clear_inputs(self):
        self.ids.principal.text = ""
        self.ids.rate.text = ""
        self.ids.periods.text = ""
        self.ids.fv_input.text = ""
        self.ids.result.text = ""

    def navigate_to(self, screen_name):
        self.manager.app.screen_history.append(screen_name)
        self.manager.current = screen_name
