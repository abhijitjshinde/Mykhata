from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineAvatarListItem, OneLineAvatarListItem, ImageLeftWidget
from kivy.properties import ListProperty, StringProperty
from kivymd.uix.snackbar import Snackbar

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu

from kivymd.uix.label import MDLabel
from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget, OneLineListItem, OneLineAvatarListItem

from kivy.network.urlrequest import UrlRequest
from kivy.app import App
import requests
import json
import ast
class customerlist(TwoLineAvatarListItem):
    icon = StringProperty()

class DialogsCustomContent(BoxLayout):
    pass
class CustomSnackbar(Snackbar):
    icon = StringProperty()

class HomeScreen(Screen):
    def Welcome_Back(self):
        CustomSnackbar(
            text="Well Come Back !",
            icon="account-circle",
            padding="20dp"            
        ).show()
    def show_snackbar(self):
        CustomSnackbar(
            text="New Customer Added",
            icon="information",
            padding="20dp",
            # button_text="ACTION",
            # button_color=(1, 0, 1, 1)
        ).show()
    # def update(self,):
    #      data = [name, phone_n]
    def Add_customer(self):
        app = App.get_running_app()
        app.root.current ='addCustomerScreen1'
        print("change zali bagh")
    
    def on_enter1(self,localId):
        app = App.get_running_app()
        AddCustomer = app.root.ids.AddCustomerScreen1.ids
        AddCustomer.Name.text = ""
        AddCustomer.Phone_Number.text = ""
        AddCustomer.drop_item.text = "Male"
        print("-------this is ids from add customer",app.root.ids.AddCustomerScreen1.ids)                
        # Get Data from Database of loclId
        # req= UrlRequest("https://as-udhar.firebaseio.com/"+ localId + ".json",self.got_data)
        # print("is UrlRequest is true?",results.data)
        results = requests.get("https://as-udhar.firebaseio.com/"+ localId + ".json")
        data = json.loads(results.content.decode())
        if data != None:
            udhari = data['customers']
            print("i am data =", udhari)   
            if udhari != "":
                keys_of_json=udhari.keys()
            else:    
                keys_of_json=udhari
            costumer_list=self.ids['costumer_list']
            # Populate Data in Screen
            for i in keys_of_json:
                profile = udhari[i]['profile'] 
                img =  ImageLeftWidget(source= profile)
                Customer_List_View=OneLineAvatarListItem(text= i,on_release=lambda x: self.set_Details_screen(x,localId))
                Customer_List_View.add_widget(img)
                costumer_list.add_widget(Customer_List_View)
        else:
            print("i am list updater else")
            pass
        
    def set_Details_screen(self,x,localId):
        app = App.get_running_app()
        app.root.current = 'accountbalance'
        print("F ka value: --------------------- " , x, "====", x.text, "----",localId)
        # results = requests.get("https://as-udhar.firebaseio.com/"+ localId +"/customers/"+ f + ".json")  
        # print("is it ok??",results.ok)
        # data = json.loads(results.content.decode())
        # print(data," from back to detail")

    # Add Customer to Database
    # def Add_Customer(self):
    #     m =DialogsCustomContent()
    #     Name = m.ids.name
    #     phone = m.ids.phone_n
    #     print(str(Name.text),"-------this is name")
    #     print(str(phone.text),"-------this is name")
    # def show_add_Costumer_form(self,**args):
              
    #     OK = [
    #         MDFlatButton(
    #         text="CANCEL",
    #         text_color=(10 / 255, 62 / 255, 84 / 255, 1),
    #         on_release=lambda x: self.custom_dialog.dismiss()
    #         ),
    #         MDFlatButton(
    #         text="OK",
    #         text_color=(10 / 255, 62 / 255, 84 / 255, 1),
    #         # on_release=lambda x: self.custom_dialog.dismiss()
    #         on_release=lambda x:self.Add_Customer()
    #         ),
    #     ]
    #     self.custom_dialog = MDDialog(
    #         size_hint=(0.5, 0.5),
    #         title="Add Costumer:",
    #         type="custom",
    #         content_cls=DialogsCustomContent(),
    #         buttons=OK,
    #         # events_callback=self.update,
            
    #     )
    #     self.custom_dialog.open()
        
