from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import Snackbar
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDSeparator
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem,TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.properties import StringProperty
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
import json
import requests
from json import dumps
class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Custom list item.''' 

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''
class Content(MDBoxLayout):
    '''Custom content.'''

class Add_Shop_Item(Screen):
    def call_ex(self):
        box = self.ids.box1       
        box.add_widget(
            MDExpansionPanel(
                icon="add-image.png",
                content=Content(),
                panel_cls=MDExpansionPanelOneLine(
                    text="Click Here to Add New Item",                    
                )
            )
        )
        box.add_widget(
            MDSeparator()
        )
    def Back_screen(self):
        print("i am in to the function")
        app = App.get_running_app()
        app.root.current = 'accountbalance'
    def Get_Ids(self,localId,idToken):
        self.localId = localId
        self.idToken = idToken
        results = requests.get("https://as-udhar.firebaseio.com/"+ localId + "/products.json")
        data = json.loads(results.content.decode())
        self.product_data = data
        print("-------product keys------",self.product_data,"-------------end")
    def on_enter(self, *args):
        localId=self.localId
        icons = "groceries.png"
        results = requests.get("https://as-udhar.firebaseio.com/"+ localId + "/products.json")
        data = json.loads(results.content.decode())
        
        for k,v in data.items():
            li=self.ids.box1.add_widget(
                ListItemWithCheckbox(text= k,secondary_text= v, icon=icons)
            )
        return super().on_enter(*args)
    def Add_entry(self,product,price):
        product_n=product
        price = price
        localId=self.localId
        idToken = self.idToken
        self.ids.box1.clear_widgets(children=None)
        # signup_url = "https://as-udhar.firebaseio.com/"+ self.localId +"/products"
        dummy_data = {product_n :price}
        icons = "groceries.png"
        patch_request = requests.patch("https://as-udhar.firebaseio.com/" + localId + "/products.json?auth=" + idToken, data= json.dumps(dummy_data))
        # print('--------',Item,price,"-----------This is data from Entry",patch_request.ok)
        results = requests.get("https://as-udhar.firebaseio.com/"+ localId + "/products.json")
        data = json.loads(results.content.decode())          


        for k,v in data.items():
            li=self.ids.box1.add_widget(
                
                ListItemWithCheckbox(text= k,secondary_text= v, icon=icons)
            )

    def callme(self):
        print("my name is selected")