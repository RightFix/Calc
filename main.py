from kivymd.app import MDApp
from kivy.core.window import Window
from assets.calculator.calculator import Calculator
from assets.tvm.tvm import TVM
from assets.assets_val.assets_val import AssetsVal

Window.softinput_mode = "pan"


class MainApp(MDApp):
    screen_history = ["calculator_screen"]

    def build(self):
        self.title = "Financial Calculator"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Skyblue"
        return super().build()

    def on_start(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, window, key, *args):
        if key == 27:
            return self.go_back()
        return False

    def go_back(self):
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

    def on_manager(self, *args):
        self.root.bind(current=self.on_screen_change)

    def on_screen_change(self, *args):
        current = self.root.current
        if current not in self.screen_history:
            self.screen_history.append(current)
        elif self.screen_history[-1] != current:
            self.screen_history.append(current)


MainApp().run()
