from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
import math

Builder.load_file("assets/tvm/tvm.kv")


class TVM(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def calculate_future_value(self):
        try:
            p = float(self.ids.pv.text or 0)
            r = float(self.ids.rate.text or 0) / 100
            n = float(self.ids.periods.text or 0)
            if r == 0:
                fv = p
            else:
                fv = p * ((1 + r) ** n)
            self.ids.result.text = f"Future Value: {fv:,.2f}"
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_present_value(self):
        try:
            fv = float(self.ids.fv.text or 0)
            r = float(self.ids.rate.text or 0) / 100
            n = float(self.ids.periods.text or 0)
            if r == 0:
                pv = fv
            else:
                pv = fv / ((1 + r) ** n)
            self.ids.result.text = f"Present Value: {pv:,.2f}"
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_pmt(self):
        try:
            pv = float(self.ids.pv.text or 0)
            r = float(self.ids.rate.text or 0) / 100
            n = float(self.ids.periods.text or 0)
            if r == 0:
                pmt = pv / n if n > 0 else 0
            else:
                pmt = (pv * r * (1 + r) ** n) / ((1 + r) ** n - 1)
            self.ids.result.text = f"Payment: {pmt:,.2f} per period"
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_nper(self):
        try:
            pv = float(self.ids.pv.text or 0)
            fv = float(self.ids.fv.text or 0)
            r = float(self.ids.rate.text or 0) / 100
            if r == 0:
                n = -fv / pv if pv != 0 else 0
            else:
                n = math.log(fv / pv) / math.log(1 + r) if pv > 0 and fv > 0 else 0
            self.ids.result.text = f"Periods: {n:,.2f}"
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_rate(self):
        try:
            pv = float(self.ids.pv.text or 0)
            fv = float(self.ids.fv.text or 0)
            n = float(self.ids.periods.text or 0)
            if n == 0 or pv == 0 or fv == 0:
                self.ids.result.text = "Error: Invalid values"
                return
            r = (fv / pv) ** (1 / n) - 1
            self.ids.result.text = f"Rate: {r * 100:,.2f}% per period"
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_npv(self):
        try:
            rate = float(self.ids.rate.text or 0) / 100
            flows = self.ids.cashflows.text
            if not flows.strip():
                self.ids.result.text = "Error: Enter cash flows"
                return
            cashflow_list = [float(x.strip()) for x in flows.split(",")]
            npv = cashflow_list[0] if cashflow_list else 0
            for i, cf in enumerate(cashflow_list[1:], 1):
                npv += cf / ((1 + rate) ** i)
            self.ids.result.text = f"NPV: {npv:,.2f}"
        except ValueError:
            self.ids.result.text = "Error: Enter valid cash flows"

    def calculate_irr(self):
        try:
            flows = self.ids.cashflows.text
            if not flows.strip():
                self.ids.result.text = "Error: Enter cash flows"
                return
            cashflow_list = [float(x.strip()) for x in flows.split(",")]
            rate = 0.1
            for _ in range(100):
                npv = sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cashflow_list))
                derivative = sum(
                    -i * cf / ((1 + rate) ** (i + 1))
                    for i, cf in enumerate(cashflow_list)
                    if i > 0
                )
                if abs(npv) < 0.01 or derivative == 0:
                    break
                rate = rate - npv / derivative
            self.ids.result.text = f"IRR: {rate * 100:,.2f}%"
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Cannot calculate IRR"

    def calculate_loan_payment(self):
        try:
            principal = float(self.ids.pv.text or 0)
            annual_rate = float(self.ids.rate.text or 0) / 100
            years = float(self.ids.periods.text or 0)
            if years == 0 or principal == 0:
                self.ids.result.text = "Error: Enter valid loan details"
                return
            months = years * 12
            if annual_rate == 0:
                monthly_pmt = principal / months
            else:
                monthly_rate = annual_rate / 12
                monthly_pmt = (
                    principal * monthly_rate * (1 + monthly_rate) ** months
                ) / ((1 + monthly_rate) ** months - 1)
            total_interest = (monthly_pmt * months) - principal
            self.ids.result.text = (
                f"Monthly: {monthly_pmt:,.2f}\nTotal Interest: {total_interest:,.2f}"
            )
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_bond_price(self):
        try:
            face_value = float(self.ids.pv.text or 0)
            coupon_rate = float(self.ids.rate.text or 0) / 100
            years = float(self.ids.periods.text or 0)
            market_rate = float(self.ids.fv.text or 0) / 100
            if years == 0 or face_value == 0:
                self.ids.result.text = "Error: Enter valid bond details"
                return
            coupon_payment = face_value * coupon_rate
            if market_rate == 0:
                price = face_value + (coupon_payment * years)
            else:
                pv_coupons = (
                    coupon_payment * (1 - (1 + market_rate) ** -years) / market_rate
                )
                pv_face = face_value / ((1 + market_rate) ** years)
                price = pv_coupons + pv_face
            self.ids.result.text = f"Bond Price: {price:,.2f}"
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Enter valid numbers"

    def calculate_savings(self):
        try:
            monthly_deposit = float(self.ids.pv.text or 0)
            rate = float(self.ids.rate.text or 0) / 100 / 12
            months = float(self.ids.periods.text or 0)
            if months == 0:
                self.ids.result.text = "Error: Enter valid period"
                return
            if rate == 0:
                fv = monthly_deposit * months
            else:
                fv = monthly_deposit * (((1 + rate) ** months - 1) / rate)
            self.ids.result.text = f"Future Value: {fv:,.2f}"
        except (ValueError, ZeroDivisionError):
            self.ids.result.text = "Error: Enter valid numbers"

    def clear_inputs(self):
        self.ids.pv.text = ""
        self.ids.fv.text = ""
        self.ids.rate.text = ""
        self.ids.periods.text = ""
        self.ids.cashflows.text = ""
        self.ids.result.text = ""

    def navigate_to(self, screen_name):
        self.manager.current = screen_name
