from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class AssetsValScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        main_layout = BoxLayout(orientation="vertical", spacing=5, padding=5)

        app_bar = BoxLayout(size_hint_y=None, height=50, padding=10)
        app_bar.add_widget(Label(text="Asset Valuation", font_size=20, halign="left"))
        main_layout.add_widget(app_bar)

        inputs_layout = GridLayout(cols=2, size_hint_y=0.5, padding=10, spacing=10)
        inputs_layout.add_widget(Label(text="Asset Cost:", halign="right"))
        self.asset_cost_input = TextInput(
            hint_text="0", multiline=False, input_filter="float"
        )
        inputs_layout.add_widget(self.asset_cost_input)

        inputs_layout.add_widget(Label(text="Salvage Value:", halign="right"))
        self.salvage_input = TextInput(
            hint_text="0", multiline=False, input_filter="float"
        )
        inputs_layout.add_widget(self.salvage_input)

        inputs_layout.add_widget(Label(text="Useful Life (years):", halign="right"))
        self.life_input = TextInput(
            hint_text="0", multiline=False, input_filter="float"
        )
        inputs_layout.add_widget(self.life_input)

        inputs_layout.add_widget(Label(text="Year:", halign="right"))
        self.year_input = TextInput(hint_text="1", multiline=False, input_filter="int")
        inputs_layout.add_widget(self.year_input)

        main_layout.add_widget(inputs_layout)

        buttons_layout = GridLayout(
            cols=2, rows=2, size_hint_y=0.3, padding=5, spacing=10
        )
        buttons_layout.add_widget(
            Button(text="Straight Line", on_press=self.calculate_straight_line)
        )
        buttons_layout.add_widget(
            Button(text="Declining Balance", on_press=self.calculate_declining_balance)
        )
        buttons_layout.add_widget(Button(text="Clear", on_press=self.clear_inputs))
        buttons_layout.add_widget(
            Button(text="Exit", on_press=lambda x: self.go_to("calculator_screen"))
        )
        main_layout.add_widget(buttons_layout)

        self.result_label = Label(text="Result: ", font_size=18, size_hint_y=0.2)
        main_layout.add_widget(self.result_label)

        self.add_widget(main_layout)

    def calculate_straight_line(self, *args):
        try:
            cost = float(self.asset_cost_input.text or 0)
            salvage = float(self.salvage_input.text or 0)
            life = float(self.life_input.text or 0)
            if life <= 0:
                self.result_label.text = "Error: Useful life must be positive"
                return
            depreciation = (cost - salvage) / life
            self.result_label.text = f"Annual Depreciation: {depreciation:,.2f}"
        except ValueError:
            self.result_label.text = "Error: Enter valid numbers"

    def calculate_declining_balance(self, *args):
        try:
            cost = float(self.asset_cost_input.text or 0)
            salvage = float(self.salvage_input.text or 0)
            life = float(self.life_input.text or 0)
            year = int(self.year_input.text or 1)
            if life <= 0:
                self.result_label.text = "Error: Useful life must be positive"
                return
            rate = 2 / life
            for _ in range(year - 1):
                cost = cost - (cost * rate)
            depreciation = cost * rate
            if cost - depreciation < salvage:
                depreciation = max(0, cost - salvage)
            self.result_label.text = f"Year {year} Depreciation: {depreciation:,.2f}"
        except ValueError:
            self.result_label.text = "Error: Enter valid numbers"

    def clear_inputs(self, *args):
        self.asset_cost_input.text = ""
        self.salvage_input.text = ""
        self.life_input.text = ""
        self.year_input.text = "1"
        self.result_label.text = "Result: "

    def go_to(self, screen_name):
        self.manager.current = screen_name
