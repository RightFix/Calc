from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from assets.calculator.calculator import CalculatorScreen
from assets.tvm.tvm import TVMScreen
from assets.assets_val.assets_val import AssetsValScreen

Window.softinput_mode = "pan"


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CalculatorScreen(name="calculator_screen"))
        sm.add_widget(TVMScreen(name="tvm_screen"))
        sm.add_widget(AssetsValScreen(name="assets_val_screen"))
        return sm


MainApp().run()
