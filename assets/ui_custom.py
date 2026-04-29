from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle, Ellipse, Line
from kivy.uix.label import Label

class RoundedButton(Button):
    def __init__(self, radius=10, btn_color=(0.24, 0.51, 0.27, 1), **kwargs):
        self.radius = radius
        self.btn_color = btn_color
        super().__init__(**kwargs)
        self.background_normal = ""
        with self.canvas.before:
            Color(*btn_color)
            self._round_rect = RoundedRectangle(
                size=self.size, pos=self.pos, radius=[radius]
            )
        self.bind(
            pos=lambda w, *_: setattr(w._round_rect, "pos", w.pos),
            size=lambda w, *_: setattr(w._round_rect, "size", w.size),
        )


class RoundedTextInput(TextInput):
    def __init__(
        self, radius=10, bg_color=(0,0,0,0), text_color=(0, 0, 0, 0), **kwargs
    ):
        self.radius = radius
        kwargs["hint_text_color"] = (0.5, 0.5, 0.5, 1)
        kwargs["cursor_color"] = (0.24, 0.51, 0.27, 1)
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_active = ""
        self.padding = (15, 10)
        with self.canvas.after:
            Color(*bg_color)
            self._bg_rect = RoundedRectangle(
                size=self.size, pos=self.pos, radius=[radius]
            )
        self.bind(
            pos=lambda w, *_: setattr(w._bg_rect, "pos", w.pos),
            size=lambda w, *_: setattr(w._bg_rect, "size", w.size),
        )
       
class CustomBoxLayout(BoxLayout):
     def __init__(
        self, radius=10, bg_color=(1,1,1,1), text_color=(0, 0, 0, 0), **kwargs
    ):
        self.radius = radius
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_active = ""
        self.padding = (15, 10)
        with self.canvas.before:
            Color(*bg_color)
            self._bg_rect = RoundedRectangle(
                size=self.size, pos=self.pos, radius=[radius]
            )
        self.bind(
            pos=lambda w, *_: setattr(w._bg_rect, "pos", w.pos),
            size=lambda w, *_: setattr(w._bg_rect, "size", w.size),
        )

class CustomLabel(Label):
     def __init__(
        self, radius=10, bg_color=(0,0,0,0), text_color=(0, 0, 0, 0), **kwargs
    ):
        self.radius = radius
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_active = ""
        self.padding = (15, 10)
        with self.canvas.before:
            Color(*bg_color)
            self._bg_rect = RoundedRectangle(
                size=self.size, pos=self.pos, radius=[radius]
            )
        self.bind(
            pos=lambda w, *_: setattr(w._bg_rect, "pos", w.pos),
            size=lambda w, *_: setattr(w._bg_rect, "size", w.size),
        )
