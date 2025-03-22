from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.switch import Switch 
from kivy.uix.dropdown import DropDown 
from kivy.uix.button import Button
from kivy.uix.label import Label

def tvmcalc(self):
    navigation = FloatLayout()
    dropdown = DropDown()
    tvm = Button(text ='Time Value Of Money (TVM)',size_hint_y= None, height = 40)
    tvm.bind(on_press = self.go_to_screen2)
    dropdown.add_widget(tvm)
 
    basic = Button(text="Financial Calculations", font_size = 25, color="white", size_hint=(0.5, .03), top=1600,right=450)
    basic.bind(on_release= dropdown.open)
    navigation.add_widget(basic)
    self.add_widget(navigation)
        
    layout = BoxLayout()
    body = Label(text="Hello")
    layout.add_widget(body)
    self.add_widget(layout)