from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty
from kivymd.uix.snackbar import Snackbar
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.toast import toast
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget, OneLineListItem, OneLineAvatarListItem
import json
import requests

class Error_Empty_field(Snackbar):
    icon = StringProperty()

class AddCustomerScreen1(Screen):
    def on_enter(self):
        self.ids.Name.text =""
        self.ids.Phone_Number.text=""
        self.ids.drop_item.text = "Male"

    def on_enter2(self,localId,idToken):
        self.user = localId
        self.idToken = idToken
        
    def update(self,x):
        app = App.get_running_app()
        x=x
        Name = self.ids.Name.text
        Number = self.ids.Phone_Number.text
        drop_item = self.ids.drop_item.text
        if drop_item == "Male":
            profile = "male.png"
        else:
            profile = "female.png"
        
        localId = self.user
        idToken = self.idToken
        # Add item to list on HomeScreen
        costumer_list = app.root.ids.HomeScreen.ids.costumer_list
        if Name !="" and Number != "" and drop_item != "":       
            img =  ImageLeftWidget(source= "male.png")
            Customer_List_View=OneLineAvatarListItem(text= Name,on_release=lambda x: app.root.ids.HomeScreen.set_Details_screen(x,localId))
            Customer_List_View.add_widget(img)
            costumer_list.add_widget(Customer_List_View)
            # Add data to Database
            dummy_data ={Name: {"name": Name ,"number":Number,"profile": profile,"Account":""}}
            post_request = requests.patch("https://as-udhar.firebaseio.com/" + localId + "/customers.json?auth=" + idToken, data= json.dumps(dummy_data))
            # req = UrlRequest('https://as-udhar.firebaseio.com/'+ self.user +'/', self.got_json)    
            if post_request.ok == True:
                app.root.ids.HomeScreen.show_snackbar()
            app.root.current = "HomeScreen"
            # run_list = app.root.ids.HomeScreen.on_enter1(localId)
        else:
            self.Fill_Details()    
    # def got_json(self,req, result):
    #     for key, value in result['headers'].items():
    #         print('{}: {}'.format(key, value))
    def Fill_Details(self):
        Error_Empty_field(
            text="Fill All Details",
            icon="information",
            padding="20dp",
            # button_text="ACTION",
            button_color=(1, 0, 1, 1)
        ).show()
    def back_to_home(self):
        app = App.get_running_app()
        app.root.current = 'HomeScreen'

    def dropme(self):        
        menu_items = [{"icon": "human-male", "text": "Male"},{"icon": "human-female", "text": "Female"} ]
        self.smenu = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            position="center",
            callback=self.set_item,
            width_mult=4,
        )
        self.smenu.open()

    def set_item(self, instance):
        # print(instance.text,"----------this is instance")
        gender = instance.text
        mm=self.ids.drop_item.set_item(gender)
        self.ids.drop_item.text = gender
        self.smenu.dismiss()
# file manager section---------------------
    manager_open = False
    file_manager = None

    def open_file_manager(self,text_item):
        preview = False if text_item == "List" else True
        if not self.file_manager:
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager, select_path=self.select_path
            )
        self.file_manager.preview = preview
        self.file_manager.show('/')
        self.manager_open = True

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.
        :type path: str;
        :param path: path to the selected directory or file;

        """
        self.exit_manager()
        toast(path)
        # print(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager_open = False
        self.file_manager.close()







    # def dropme(self):        
    #     menu_items = [{"icon": "human-male", "text": "Male"},{"icon": "human-female", "text": "Female"} ]
    #     self.smenu = MDDropdownMenu(
    #         caller=self.ids.drop_item,
    #         items=menu_items,
    #         position="center",
    #         callback=self.set_item,
    #         width_mult=4,
    #     )
    #     self.smenu.open()

    # def set_item(self, instance):
    #     mm=self.ids.drop_item.set_item(instance.text)
    #     print(mm)
    #     self.smenu.dismiss()
# file manager section---------------------
    # manager_open = False
    # file_manager = None

    # def open_file_manager(self,text_item):
    #     preview = False if text_item == "List" else True
    #     if not self.file_manager:
    #         self.file_manager = MDFileManager(
    #             exit_manager=self.exit_manager, select_path=self.select_path
    #         )
    #     self.file_manager.preview = preview
    #     self.file_manager.show('/')
    #     self.manager_open = True

    # def select_path(self, path):
    #     """It will be called when you click on the file name
    #     or the catalog selection button.
    #     :type path: str;
    #     :param path: path to the selected directory or file;

    #     """
    #     self.exit_manager()
    #     toast(path)
    #     # print(path)

    # def exit_manager(self, *args):
    #     """Called when the user reaches the root of the directory tree."""

    #     self.manager_open = False
    #     self.file_manager.close()