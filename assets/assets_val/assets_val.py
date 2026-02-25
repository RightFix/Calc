from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel

Builder.load_file("assets/assets_val/assets_val.kv")


class AssetsVal(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def calculate_straight_line(self):
        try:
            cost = float(self.ids.asset_cost.text or 0)
            salvage = float(self.ids.salvage_value.text or 0)
            life = float(self.ids.useful_life.text or 0)
            if life <= 0:
                self.ids.result.text = "Error: Useful life must be positive"
                return
            depreciation = (cost - salvage) / life
            self.ids.result.text = f"Annual Depreciation: {depreciation:,.2f}"
        except ValueError:
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_declining_balance(self):
        try:
            cost = float(self.ids.asset_cost.text or 0)
            salvage = float(self.ids.salvage_value.text or 0)
            life = float(self.ids.useful_life.text or 0)
            year = int(self.ids.year_input.text or 1)
            if life <= 0:
                self.ids.result.text = "Error: Useful life must be positive"
                return
            rate = 2 / life
            for _ in range(year - 1):
                cost = cost - (cost * rate)
            depreciation = cost * rate
            if cost - depreciation < salvage:
                depreciation = max(0, cost - salvage)
            self.ids.result.text = f"Year {year} Depreciation: {depreciation:,.2f}"
        except ValueError:
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_roi(self):
        try:
            gain = float(self.ids.gain.text or 0)
            cost = float(self.ids.asset_cost.text or 0)
            if cost == 0:
                self.ids.result.text = "Error: Cost cannot be zero"
                return
            roi = ((gain - cost) / cost) * 100
            self.ids.result.text = f"ROI: {roi:,.2f}%"
        except ValueError:
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_npv(self):
        try:
            rate = float(self.ids.rate.text or 0) / 100
            cashflows = self.ids.cashflows.text
            if not cashflows.strip():
                self.ids.result.text = "Error: Enter cash flows"
                return
            flows = [float(x.strip()) for x in cashflows.split(",")]
            npv = sum(flow / ((1 + rate) ** (i + 1)) for i, flow in enumerate(flows))
            self.ids.result.text = f"NPV: {npv:,.2f}"
        except ValueError:
            self.ids.result.text = "Error: Enter valid cash flows"

    def calculate_irr(self):
        try:
            cashflows = self.ids.cashflows.text
            if not cashflows.strip():
                self.ids.result.text = "Error: Enter cash flows"
                return
            flows = [float(x.strip()) for x in cashflows.split(",")]
            rate = 0.1
            for _ in range(100):
                npv = sum(flow / ((1 + rate) ** (i + 1)) for i, flow in enumerate(flows))
                if abs(npv) < 0.01:
                    break
                derivative = sum(-(i + 1) * flow / ((1 + rate) ** (i + 2)) for i, flow in enumerate(flows))
                if derivative == 0:
                    break
                rate = rate + npv / derivative
            self.ids.result.text = f"IRR: {rate * 100:,.2f}%"
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Cannot calculate IRR"

    def clear_inputs(self):
        self.ids.asset_cost.text = ""
        self.ids.salvage_value.text = ""
        self.ids.useful_life.text = ""
        self.ids.year_input.text = ""
        self.ids.gain.text = ""
        self.ids.rate.text = ""
        self.ids.cashflows.text = ""
        self.ids.result.text = ""

    def navigate_to(self, screen_name):
        self.manager.app.screen_history.append(screen_name)
        self.manager.current = screen_name
