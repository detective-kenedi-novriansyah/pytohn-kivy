from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from app.auth.loginscreen import LoginScreen
from app.auth.registerscreen import RegisterScreen

class MainApp(App):
    def __init__(self):
        App.__init__(self)
        self.sm = ScreenManager()
        self.lg = LoginScreen(self, self.sm)
        self.rg = RegisterScreen(self, self.sm)
    
    def build(self):
        self.s = Screen(name="Login")
        self.s.add_widget(self.lg)
        self.sm.add_widget(self.s)

        self.sx = Screen(name="Register")
        self.sx.add_widget(self.rg)
        self.sm.add_widget(self.sx)

        return self.sm