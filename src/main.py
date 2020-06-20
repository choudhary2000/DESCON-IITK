from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import re

pattern = re.compile("[0-9]+")
digit = list()
operator = list()        

class AddButton(GridLayout,Button):
    def __init__(self,name,**kwargs):
        super(AddButton,self).__init__(**kwargs)
        self.cols = 1
        self.rows = 1
        self.name = name
        self.btn = Button(text = self.name)
        self.btn.bind(on_press=self.callback)
        self.add_widget(self.btn)
    def callback(self,instance):
        if bool(pattern.fullmatch(instance.text)):
            digit.append(int(instance.text))
        else:
            if instance.text != "=":
                operator.append(instance.text)
            else:
                pass
class Layout2(GridLayout):
    def __init__(self,**kwargs):
        super(Layout2,self).__init__(**kwargs)
        self.cols = 4
        self.add_widget(AddButton('7'))
        self.add_widget(AddButton('8'))
        self.add_widget(AddButton('9'))
        self.add_widget(AddButton('/'))
        self.add_widget(AddButton('4'))
        self.add_widget(AddButton('5'))
        self.add_widget(AddButton('6'))
        self.add_widget(AddButton('*'))
        self.add_widget(AddButton('1'))
        self.add_widget(AddButton('2'))
        self.add_widget(AddButton('3'))
        self.add_widget(AddButton('+'))
        self.add_widget(AddButton('0'))
        self.add_widget(AddButton('.'))
        self.add_widget(AddButton('%'))
        self.add_widget(AddButton('-'))
        self.add_widget(AddButton('='))

class Layout1(GridLayout):
    def __init__(self,**kwargs):
        super(Layout1,self).__init__(**kwargs)
        self.rows = 2
        self.padding = [50,100,50,50]
        self.spacing = [10,10]
        self.label = Label(text='0')
        self.label.bind(on_press=self.callback)
        self.add_widget(self.label)
        layout_ = Layout2()
        self.add_widget(layout_)
    def callback(self,instance):
        print("Hello")



class Myapp(App):
    def build(self):
        return Layout1()        

if __name__ == '__main__':
    Myapp().run()
