
from feature1 import UserManage
from feature2 import Goals
from feature3 import Daily_Logger
from scoring import calculate_daily_score
from streak import update_streak
from data_manager import get_data, set_data

def main_menu():
    print("\nTiny Believer options :")
    print("1=Register")
    print("2=Login")
    print("3=Set today's Goals")
    print("4=Log today's Progress")
    print("5=Show Progress Dashboard")
    print("6=Exit")
    choice = input("plz enter your choice").strip()
    return choice

def main():
    user_manager = UserManage()
    goals_feature = Goals()
    logger_feature = Daily_Logger()

    while True:
        choice = main_menu()

        match choice:
            case "1":
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                user_manager.register(username, password)

            case "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                if user_manager.login(username, password):
                    goals_feature.current_user = username
                    logger_feature.current_user = username
                else:
                    print("Login failed.")

            case "3":
                if not user_manager.current_user:
                    print("Plz login first!")
                else:
                    goals_feature.set_d_goals()

            case "4":
                if not user_manager.current_user:
                    print("Plz login first!")
                else:
                    if logger_feature.done_goals():
                        data = get_data()
                        user_data = data["users"][user_manager.current_user]
                        last_date = user_data.get("last_login_date", "")
                        current_streak = user_data.get("streak", 0)
                        new_streak, today_str = update_streak(current_streak, last_date)
                        user_data["streak"] = new_streak
                        user_data["last_login_date"] = today_str

                        daily_score = calculate_daily_score(user_data["daily_record"], new_streak)
                        user_data["total_score"] += daily_score

                        set_data(data)

            case "5":
                if not user_manager.current_user:
                    print("Plz login first!")
                else:
                    data = get_data()
                    user_data = data["users"][user_manager.current_user]
                    from progress import show_progress
                    show_progress(user_data)

            case "6":
                print("Bye👋 see u soon ")
                break

            case _:
                print("invalid choice try again!")

if __name__ == "__main__":
    main()
