if __name__ == "__main__":
    from kivymd.app import MDApp
    from kivy import utils
    from kivy.lang import Builder
    import requests
    import json

    # -- This import can be done in kv lang or python
    from homescreen import HomeScreen 
    from AddCustomerScreen import AddCustomerScreen1
    from accountbalance import AccountBalance
    from addshopitemscreen import Add_Shop_Item
    from json import dumps
    import sys
    import os.path
    sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
    # Load the kv files
    folder = os.path.dirname(os.path.realpath(__file__))
    Builder.load_file(folder + "/homescreen.kv")
    Builder.load_file(folder + "/AddCustomerScreen.kv")
    Builder.load_file(folder + "/accountbalance.kv")
    Builder.load_file(folder + "/addshopitemscreen.kv")
     
    class MainApp(MDApp):
        def on_start(self):
            self.root.ids.addshopitemscreen.call_ex()
        def user_localId(self,localId):
            localId = localId
            # results = requests.get("https://as-udhar.firebaseio.com/"+ localId + ".json")
            # print("is it ok??",results.ok)
            # data = json.loads(results.content.decode())
            print(localId,"user update")
            return localId
        # def Add_customer(self, product, qunt, price):
        #     data = [product, qunt, price]
        #     print(data)
        # user=user_localId.localId
        # print(user,"-------this is user id")

        # dummy_data = '{"name":"kali kirana","customers":{"name":"sadhu","number":"","udhari":{"item":"oil","price":"","quantity":""}}}'
        # post_request = requests.patch("https://as-udhar.firebaseio.com/" + user_id + ".json?auth=" + idToken, data= dummy_data)
        pass
 
            
    MainApp().run()