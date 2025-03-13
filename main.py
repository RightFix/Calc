from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.switch import Switch 
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.add_widget(Screen1(name='screen1'))
        self.add_widget(Screen2(name='screen2'))
        self.add_widget(Screen3(name='screen3'))
        
class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', )
        output = Label(text="",font_size=55, color="white",bold=True, size_hint=(1,1.8), halign="right", text_size=(650,650), valign="bottom",padding=(0,0),)
        
        result = Label(text="",font_size=35, color="white",bold=False, center=(0,0),size_hint=(1,0.2), halign="right", valign="bottom", text_size=(650,50))
       
        layout.add_widget(output)
        layout.add_widget(result)
        body = GridLayout(rows= 5, cols=4)
        
        clear = Button(text ="C", bold= True, font_size= 30)
        def clr(instance):
          output.text =  ""
          return output.text
        clear.bind(on_press= clr)
        body.add_widget(clear)
        
        divide = Button(text ="÷", bold= True, font_size= 30)
        def div(instance):
          output.text +=  "÷"
          return output.text
        divide.bind(on_press= div)
        body.add_widget(divide)
        
        multiply = Button(text ="×", bold= True, font_size= 30)
        def mul(instance):
          output.text +=  "×"
          return output.text
        multiply.bind(on_press= mul)
        body.add_widget(multiply)
        
        delete = Button(text ="del", bold= True, font_size= 30)
        def dele (instance):
          if len(output.text) > 0:  
           output.text = str(output.text)[0:-1]
           return output.text
        delete.bind(on_press= dele)
        body.add_widget(delete)
        
        num7 = Button(text ="7", bold= True, font_size= 30)
        def seven(instance):
          output.text +=  "7"
          return output.text
        num7.bind(on_press= seven)
        body.add_widget(num7)
        
        num8 = Button(text ="8", bold= True, font_size= 30)
        def eight(instance):
          output.text +=  "8"
          return output.text
        num8.bind(on_press=eight)
        body.add_widget(num8)
        
        num9 = Button(text ="9", bold= True, font_size= 30)
        def nine(instance):
          output.text +=  "9"
          return output.text
        num9.bind(on_press= nine)
        body.add_widget(num9)
        
        minus = Button(text ="-", bold= True, font_size= 30)
        def subtract(instance):
          output.text +=  "-"
          return output.text
        minus.bind(on_press= subtract)
        body.add_widget(minus)
        
        num4 = Button(text ="4", bold= True, font_size= 30)
        def four(instance):
          output.text +=  "4"
          return output.text
        num4.bind(on_press= four)
        body.add_widget(num4)
        
        num5 = Button(text ="5", bold= True, font_size= 30)
        def five(instance):
          output.text +=  "5"
          return output.text
        num5.bind(on_press= five)
        body.add_widget(num5)
        
        num6 = Button(text ="6", bold= True, font_size= 30)
        def six(instance):
          output.text +=  "6"
          return output.text
        num6.bind(on_press= six)
        body.add_widget(num6)
        
        plus = Button(text ="+", bold= True, font_size= 30)
        def add(instance):
          output.text +=  "+"
          return output.text
        plus.bind(on_press= add)
        body.add_widget(plus)
        
        num1 = Button(text ="1", bold= True, font_size= 30)
        def one(instance):
          output.text +=  "1"
          return output.text
        num1.bind(on_press= one)
        body.add_widget(num1)
        
        num2 = Button(text ="2", bold= True, font_size= 30)
        def two(instance):
          output.text +=  "2"
          return output.text
        num2.bind(on_press= two)
        body.add_widget(num2)
        
        num3 = Button(text ="3", bold= True, font_size= 30)
        def three(instance):
          output.text +=  "3"
          return output.text
        num3.bind(on_press= three)
        body.add_widget(num3)
        
        equal = Button(text ="=", bold= True, font_size= 30)
        def solve(instance):
          try: 
              check1 = output.text.replace("×","*")  
              check2 = check1.replace("÷","/")
              soln = eval(check2)
              output.text = str(soln)
              result.text = str(soln)
              return output.text, result.text
          except SyntaxError:
               output.text = output.text
               result.text = "Error"
               return output.text, result.text    
        equal.bind(on_press= solve)
        body.add_widget(equal)
        
        percent = Button(text ="%", bold= True, font_size= 30)
        def perc(instance):
          try:
             if len(output.text) > 0:
                   output.text =  str(float(output.text) * 0.01)
                   return output.text
          except ValueError:
               output.text = output.text
               result.text = "Error"
               return output.text, result.text    
        percent.bind(on_press= perc)
        body.add_widget(percent)
        
        num0 = Button(text ="0", bold= True, font_size= 30)
        def zero(instance):
          output.text +=  "0"
          return output.text
        num0.bind(on_press= zero)
        body.add_widget(num0)
        
        point = Button(text =".", bold= True, font_size= 30)
        def poin(instance):
          if "." not in str(output.text):
           output.text +=  "."
           return output.text
        point.bind(on_press= poin)
        body.add_widget(point)
        
        more = Button(text ="more", bold= True, font_size= 30)
        body.add_widget(more)
        
        layout.add_widget(body)
        self.add_widget(layout)
        

    def go_to_screen2(self, instance):
        self.manager.current = 'screen2'
    def go_to_screen3(self, instance):
        self.manager.current = 'screen3'
      

class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        layout = BoxLayout(orientation="horizontal")
        # header
        self.add_widget(layout)

    def go_to_screen1(self, instance):
        self.manager.current = 'screen1'
    def go_to_screen2(self, instance):
        self.manager.current = 'screen2'
    def go_to_screen3(self, instance):
        self.manager.current = 'screen3'
        
class Screen3(Screen):
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        # header
        self.add_widget(layout)

    def go_to_screen1(self, instance):
        self.manager.current = 'screen1'
    def go_to_screen2(self, instance):
        self.manager.current = 'screen2'
    def go_to_screen3(self, instance):
        self.manager.current = 'screen3'
      

class calc(App):
    def build(self):
      return MyScreenManager()

if __name__ == '__main__':
    calc().run()