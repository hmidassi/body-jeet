import kivy
from dbConnection import dbConnection
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class BodyJeet(Widget):
    pass

class BodyJeetApp(App):
    def build(self):
        connectionManager=dbConnection("dbAppliBodyJeet")
        conn=connectionManager.createConnection()
        cursor=connectionManager.createCursor(conn)
        cursor.execute("SELECT * FROM CATEGORIE_EXERCICE")
        exercice=""
        for line in cursor:
            exercice=exercice+line[1]+"\n"
        return Label(text=exercice)

app=BodyJeetApp()
if __name__=='__main__':
    app.run()