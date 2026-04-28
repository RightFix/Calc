from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from assets.calculator.calculator import CalculatorScreen
from assets.tvm.tvm import TVMScreen
from assets.assets_val.assets_val import AssetsValScreen
from assets.scientific.scientific import SciScreen

Window.softinput_mode = "pan"


class CalculatorApp(App):
    """
    This is the Calculator app"""

    screen_history = ["calculator_screen"]

    def build(self):
        sm = ScreenManager()
        sm.add_widget(CalculatorScreen(name="calculator_screen"))
        sm.add_widget(SciScreen(name="sci_screen"))
        sm.add_widget(TVMScreen(name="tvm_screen"))
        sm.add_widget(AssetsValScreen(name="assets_val_screen"))
        return sm

    def go_back(self):
        """The Go back logic"""
        current = self.root.current
        if current != "calculator_screen":
            if len(self.screen_history) > 1:
                self.screen_history.pop()
                self.root.current = self.screen_history[-1]
            else:
                self.root.current = "calculator_screen"
            return True
        else:
            self.stop()
            return True

    def on_start(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, window, key, *args):
        """
        This is for the back  button
        """
        if key == 27:
            return self.go_back()
        return False


CalculatorApp().run()
