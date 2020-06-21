from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import math
import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import AsyncImage
from kivy.core.window import Window

class CalGrid(GridLayout):
    def __init__(self,**kwargs):
        super(CalGrid,self).__init__(**kwargs)
        self.cols = 1
        self.operators = ["+", "-", "*", "/","sin", "cos", "tan", "exp", "asin", "acos", "atan", "log10", "log", "pi", "sqrt"]
        self.last_was_operator = None
        self.last_button = None
        self.solution = TextInput(multiline = False, readonly = True, halign = "right", font_size = 55, size_hint = (1, 0.2), pos_hint = {'x': 0, 'y': 0.8})
        self.add_widget(self.solution)
        
        buttons = [
            ["sin", "cos", "tan", "exp", "log"],
            ["asin", "acos", "atan", "log10", "sqrt"],
            ["(", "7", "8", "9", "/"],
            [")", "4", "5", "6", "*"],
            ["pi", "1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        
        self.keys = GridLayout()
        self.keys.size_hint = (1, .8)
        self.keys.pos_hint = {'x' : 0, 'y' : 0}
        self.keys.cols = 5
        for row in buttons:
            
            for label in row:
                button = Button(
                    text = label,
                    pos_hint = {"centre_x" : 0.5, "centre_y" : 0.5},
                    
                )
                button.bind(on_press = self.pressed)
                self.keys.add_widget(button)
        equal_button = Button(text = "=")
        equal_button.bind(on_press = self.on_solution)
        self.keys.add_widget(equal_button)
        
        self.add_widget(self.keys)
    
    
    def pressed(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            self.solution.text = ""
        
        else:
            if current and (self.last_was_operator and button_text in ["+", "-", "*", "/"]):
                return
            elif current == "" and button_text in ["+", "-", "*", "/"]:
                return
            else:
                if button_text in ["sin", "cos", "tan", "asin", "acos", "atan", "log10", "log", "pi", "exp", "sqrt"]:
                    new_text = current + "{}".format("math.")+ button_text
                    self.solution.text = new_text
                    
                else:
                    new_text = current + button_text
                    self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in ["+", "-", "*", "/"]
    def on_solution(self, instance):
        text=self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


class FPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        
        self.add_widget(AsyncImage(source = "https://png.pngtree.com/png-clipart/20190614/original/pngtree-calculator-icon-png-image_3715103.jpg", size_hint = (1, .9)),)

        self.btn = Button(text = "Calculate", font_size = 50, size_hint = (1, .1), background_color = (0, 255, 0, .8) )
        self.btn.bind(on_press = self.do)
        self.add_widget(self.btn)

    def do(self,instance):
        calc_app.screen_manager.current = "calculate"
    

class Calculator(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        self.screen_manager = ScreenManager()
        
        self.fpage = FPage()
        screen = Screen(name = "FirstPage")
        screen.add_widget(self.fpage)
        self.screen_manager.add_widget(screen)
        
        self.maincalc = CalGrid()
        screen = Screen(name = "calculate")
        screen.add_widget(self.maincalc)
        self.screen_manager.add_widget(screen)
        return self.screen_manager

if __name__=="__main__":
    calc_app = Calculator()
    calc_app.run()
    