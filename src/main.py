from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.boxlayout import BoxLayout
#from kivy.properties import ObjectProperty
import math
import ast
#import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class CalGrid(GridLayout):
    def __init__(self,**kwargs):
        super(CalGrid,self).__init__(**kwargs)
        
        self.padding = [5, 5, 5, 5]
        self.spacing = [2.5]
        self.cols = 1
        self.operators = ["+", "-", "*", "/","sin", "cos", "tan", "exp", "asin", "acos", "atan", "log10", "log", "pi", "sqrt", ".", "("]
        self.last_was_operator = None
        self.last_button = None
        self.new_text = ""
        self.new_text_list = []
        self.solution_text_list = []
        self.solution = TextInput(multiline = True, readonly = True, halign = "right", font_size = 55, size_hint = (1, 0.125), pos_hint = {'x': 0, 'y': 0.875})
        self.solution.padding = [5,15,20,5]
        self.add_widget(self.solution)
        
        buttons = [
            ["sin", "cos", "tan", "exp", "sqrt"],
            ["asin", "acos", "atan", "ln", "log10"],
            ["7", "8", "9", "/","C"],
            ["4", "5", "6", "*","<-"],
            ["1", "2", "3", "+","("],
            ["0", ".", "pi", "-", ")"]
        ]
        
        self.keys = GridLayout(spacing = [2.5])
        self.keys.size_hint = (1, .750)
        self.keys.pos_hint = {'x' : 0, 'y' : .125}
        self.keys.cols = 5
        for row in buttons:          
            for label in row:
                button = Button(
                    text = label,
                    pos_hint = {"centre_x" : 0.5, "centre_y" : 0.5},
                    font_size = 20               
                )
                button.bind(on_press = self.pressed)
                self.keys.add_widget(button)
        self.add_widget(self.keys)
        equal_button = Button(text = "=", size_hint = (1, .125))
        equal_button.bind(on_press = self.ans)
        self.add_widget(equal_button)
    
    def pressed(self, instance):
         button_text = instance.text
         current = self.solution.text
         
         if button_text == "<-":
            if current == "":
                return
            else: 
                self.solution_text_list.pop()
                self.new_text_list.pop()
                self.new_text = "".join(self.new_text_list)
                self.solution.text = "".join(self.solution_text_list)
        
         else:
            if button_text == "C" or self.solution.text == 'ERROR' :
                self.solution.text = ""
                self.new_text = ""
                self.new_text_list = []
                self.solution_text_list = []
            else:
                if current and (self.last_was_operator and button_text in ["+", "-", "*", "/", "."]):
                    return
                elif button_text == "(":
                    if (current != "" and self.new_text_list[len(self.new_text_list) - 1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "pi", ")"]):
                        self.new_text = "".join(self.new_text_list) + "*" + button_text 
                        new_text_on_bar = current + "*" + button_text
                        self.solution.text = new_text_on_bar 
                        self.solution_text_list.append("*" + button_text)  
                        self.new_text_list.append("*" + button_text)
                    
                elif current == "" and button_text in ["+", "*", "/", ")"]:
                    return
                elif button_text == ")" and ((self.new_text_list[len(self.new_text_list) - 1] in ["math.sin(", "math.cos(", "math.tan(", "math.asin(", "math.acos(", "math.atan(", "math.log10(", "math.log(", "math.exp(", "math.sqrt("]) or (current != "" and self.new_text_list[len(self.new_text_list) - 1] == "(")):
                    return
                elif button_text == "pi":
                    self.new_text = "".join(self.new_text_list) + "{}".format("*math.")+ button_text 
                    new_text_on_bar = current + button_text 
                    self.solution.text = new_text_on_bar 
                    self.solution_text_list.append(button_text) 
                    self.new_text_list.append("math." + button_text)
                else:
                    if button_text in ["sin", "cos", "tan", "asin", "acos", "atan", "log10", "log", "exp", "sqrt"]: 
                        if current != "" and self.new_text_list[len(self.new_text_list) - 1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")"]:
                            self.new_text = "".join(self.new_text_list) + "{}".format("*math.")+ button_text + "("
                            new_text_on_bar = current + "*" + button_text + "("
                            self.solution.text = new_text_on_bar 
                            self.solution_text_list.append("*" + button_text + "(") 
                            self.new_text_list.append("*math." + button_text + "(")                                                         
                        else:                                                         
                            self.new_text = "".join(self.new_text_list) + "{}".format("math.")+ button_text + "("
                            new_text_on_bar = current + button_text + "("
                            self.solution.text = new_text_on_bar 
                            self.solution_text_list.append(button_text + "(") 
                            self.new_text_list.append("math." + button_text + "(")  
    
                        
                    else:
                        new_text_on_bar = current + button_text
                        self.solution.text = new_text_on_bar
                        self.new_text = "".join(self.new_text_list) + button_text
                        self.solution_text_list.append(button_text)
                        self.new_text_list.append(button_text)
         self.last_button = button_text
         self.last_was_operator = self.last_button in ["+", "-", "*", "/", "."]
    def ans(self, instance):
        def is_valid_python(code):
            try:
                ast.parse(code)
            except (SyntaxError, TypeError):
                    return False
            return True
        
        if is_valid_python(self.new_text)  == True:
            if self.new_text and self.new_text_list[len(self.new_text_list) - 1]  not in self.operators :
                self.solution.text = str(eval(self.new_text))     
        else:
            self.solution.text = 'ERROR'
        

class FPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        lbl = Label(text = "BASIC\nSCIENTIFIC\nCALCULATOR")
        lbl.pos_hint = {'x' : .25, 'y' : .4}
        lbl.size_hint = (.5, .4)
        lbl.font_size = 70
        lbl.color = (0, 255, 0, 1)
        self.add_widget(lbl)

        btn = Button(text = "CALCULATE", font_size = 30, size_hint = (.6, .1), pos_hint = {'x' : .2, 'y' : .2}, background_color = (0, 0, 0, .8) )
        btn.bind(on_press = self.do)
        self.add_widget(btn)
        lbl1 = Label(text = "Enter angle in radians", pos_hint = {'x' : .1, 'y' : 0}, size_hint = (.8, .05), font_size = 20, color = (0, 255, 0, 1), halign = "center")
        self.add_widget(lbl1)
        
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
