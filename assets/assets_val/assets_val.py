from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle


class AssetsValScreen(Screen):
    HEADER_COLOR = (0.25, 0.45, 0.25, 1)
    BG_COLOR = (0.95, 0.95, 0.95, 1)
    BTN_COLOR = (0.3, 0.6, 0.3, 1)
    INPUT_BG = (0.85, 0.85, 0.85, 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        main_layout = BoxLayout(
            orientation="vertical", spacing=10, padding=[15, 10, 15, 10]
        )

        app_bar = BoxLayout(size_hint_y=None, height=50, padding=15)
        header = Label(
            text="[b]Asset Valuation[/b]",
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
            background_color=self.BTN_COLOR,
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

        top_nav.add_widget(calc_btn)
        top_nav.add_widget(assets_btn)
        top_nav.add_widget(tvm_btn)

        main_layout.add_widget(app_bar)
        main_layout.add_widget(top_nav)

        inputs_layout = BoxLayout(
            orientation="vertical", size_hint_y=0.40, spacing=15, padding=10
        )

        inputs_config = [
            ("Asset Cost:", "0"),
            ("Salvage Value:", "0"),
            ("Useful Life (years):", "0"),
            ("Year:", "1"),
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
                cursor_color=(0.3, 0.6, 0.3, 1),
                size_hint_x=0.65,
            )
            row.add_widget(lbl)
            row.add_widget(inp)
            inputs_layout.add_widget(row)
            if label_text == "Asset Cost:":
                self.asset_cost_input = inp
            elif label_text == "Salvage Value:":
                self.salvage_input = inp
            elif label_text == "Useful Life (years):":
                self.life_input = inp
            else:
                self.year_input = inp

        main_layout.add_widget(inputs_layout)

        buttons_layout = GridLayout(
            cols=2, rows=2, size_hint_y=0.25, padding=10, spacing=12
        )
        buttons_config = [
            ("Straight Line", self.calculate_straight_line),
            ("Declining Balance", self.calculate_declining_balance),
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
            text="Select calculation method",
            font_size=16,
            size_hint_y=0.20,
            halign="center",
            color=(0.2, 0.2, 0.2, 1),
        )
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
            year = int(float(self.year_input.text or 1))
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
        self.result_label.text = "Select calculation method"

    def go_to(self, screen_name):
        self.manager.current = screen_name
