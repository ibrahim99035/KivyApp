from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen

Window.clearcolor=(0,0,0,1)
Window.size=(450,600)


class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('my.kv')

class MyMainApp(App):
    def build(self):
        self.title='wdah app'
        return kv

if __name__ == '__main__':
    MyMainApp().run()
