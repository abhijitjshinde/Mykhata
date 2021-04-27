from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import Snackbar
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.app import App


class AccountBalance(Screen):
    def Add_Items(self):
        app = App.get_running_app()
        app.root.current = 'addshopitemscreen'
