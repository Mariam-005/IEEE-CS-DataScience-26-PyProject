from data_manager import get_data, set_data
from feature1 import UserManage

class Goals(UserManage):
    def __init__(self):
        super().__init__()

    def set_d_goals(self):
        if not self.current_user:
          print("Hey Fighter, plz you need to login first")
          return False

        print("Set your intentions for today ")
        is_fasting = input("Are you fasting today? (yes/no): ").strip().lower()

        if is_fasting not in ['yes', 'no']:
            print("Plz only 'yes' or 'no' answer")
            return False
        
        try:
            print("let's set your goals ")
            q_pages =int(input("How many quran pages are u gonna read today? "))
            d_count =int(input("How many dhikr counts? "))
            h_mom   =int(input("How many times will you help at home? "))


            d_intentions = {
                "is_Fasting": True
                if is_fasting == "yes" else False, 
                "prayers_count": 5,  
                "quran_pages": q_pages,
                "dhikr_count": d_count,
                "helping_mom": h_mom
            }

            data = get_data()
            data["users"][self.current_user]["goals"] = d_intentions
            
            if set_data(data):
                print(f"intentions saved keep fighting see u soon {self.current_user} \U0001F525")
                return True
            else:
                print("Smth went wrong Please try again.")
                return False
        except ValueError:
            print("Invalid input ")
            return False
        
