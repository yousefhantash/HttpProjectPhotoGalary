from definition import *
import json

class Login:

    # Constructor
    def __init__(self):
        pass

   
    def login(self,username,password):
        data = {}
        logincreds = self.getcredentials()

        for key in logincreds:
            if logincreds[key]['user'] == username and logincreds[key]['password'] == password:
                data['type'] = logincreds[key]['type']
                data['result'] = True

                return data
        return False

    
    def logout(self):
        pass

   
    def getcredentials(self):
        data = json.loads(open(CREDENTIALS_FILE).read())
        return data['credentials']
