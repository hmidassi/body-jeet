import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class BodyJeet(Widget):
    pass

class BodyJeetApp(App):
    def build(self):
        return Label(text='Salut le monde')

app=BodyJeetApp()
if __name__=='__main__':
    app.run()