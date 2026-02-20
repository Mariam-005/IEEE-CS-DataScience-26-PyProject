from data_manager import get_data, set_data

class UserManage:
    def __init__(self):
        self.current_user = None

    def is_empty(self, username, password):
        return not username.strip() or not password.strip()
    
    def user_exist(self, username): 
        data = get_data()
        return username in data["users"]
    


    def register(self, username, password):
        if self.is_empty(username, password):
            print("Username and Password can not be empty")
            return False
        
        if self.user_exist(username):
            print("sorry this username is already taken try another one")
            return False

        data = get_data()
      
        data["users"][username] = {
            "password": password,
            "goals": {},
            "daily_record": {},
            "total_score": 0,
            "streak": 0
        }
        
        if set_data(data):
            print(f"Welcome {username} your adventure as a Tiny Believer begins now. Keep your streak alive! \U0001F525")#fire emoji unicode
            return True
        else:
            print("Plz try again data hasn't been saved")
            return False

    def login(self, username, password):
        if self.is_empty(username, password):
            print("Username and Password cannot be empty")
            return False

        data = get_data()
     
        if self.user_exist(username) and data["users"][username]["password"] == password:
            self.current_user= username
            print(f"Welcome back, Believer {username}")
            print("The world is ready for your progress..Are u ready for today's challenge?")
            return True
        else:
            print("sorry something went wrong with username or password")
            return False
