from kivy.uix.boxlayout import BoxLayout

class RegisterScreen(BoxLayout):
    def __init__(self,parent,controller):
        parent.load_kv('app/templates/registerscreen.kv')
        self.ctrl = controller
        BoxLayout.__init__(self)

    def instance_r(self):
        self.ctrl.current = "Login"