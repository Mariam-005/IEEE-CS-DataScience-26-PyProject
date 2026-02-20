from data_manager import get_data, set_data
from feature2 import Goals

class Daily_Logger(Goals):
    def __init__(self):
        super().__init__()

    def done_goals(self):
        if not self.current_user:
            print("plz login first ")
            return False

        print("your progress Report :")
        
        try:
            did_fast= input("did you complete your fast today ,fighter? (yes/no): ").strip().lower()
            if did_fast not in ["yes", "no"]:
                print("Plz answer only 'yes' or 'no'.")
                return False

            p_done = int(input("How many prayers did u do? "))
            q_done = int(input("How many Quran pages did u read? "))
            d_done = int(input("How many Dhikr counts finished "))
            h_done = int(input("How many times did you help at home? "))
            if any(i < 0 for i in [p_done, q_done, d_done, h_done]):
                print("goals cannot be negative")
                return False

            done_record = {
                "fasted": True if did_fast == "yes" else False,
                "prayers_done":p_done,
                "quran_done":q_done,
                "dhikr_done":d_done,
                "helping_done": h_done
            }

            data = get_data()
            data["users"][self.current_user]["daily_record"] = done_record

            if set_data(data):
                print("Great job! your progress has been recorded ")
                return True
            else:
                print("Smth went wrong plz try again ")
                return False

        except ValueError:
            print("Invalid input")
            return False
