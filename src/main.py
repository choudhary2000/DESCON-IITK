from kivy.app import App 
from kivy.uix.widget import Widget

class Myapp(App):
    def build(self):
        root = Widget()
        return root

if __name__ == '__main__':
    Myapp().run()