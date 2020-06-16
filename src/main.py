from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class button_layout(GridLayout):
    def __init__(self,*args,**kwargs):
        super(button_layout,self).__init__(*args, **kwargs)
        self.cols = 1
        self.add_widget(Button(text='Hello'))
        self.add_widget(Button(text='World')) 

class MyApp(App):
    def build(self):
        return button_layout()

if __name__ == '__main__':
    MyApp().run()