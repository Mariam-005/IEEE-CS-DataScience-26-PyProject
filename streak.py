from datetime import datetime

def update_streak(current_streak, last_login_date):
    
    today = datetime.now().date()
    today_str = str(today)

    if not last_login_date:
        return 1, today_str

    try:
        last_date = datetime.strptime(last_login_date, "%Y-%m-%d").date()

    except ValueError:
        return 1, today_str

    difference = (today - last_date).days

    new_streak = current_streak

    if difference == 0:
        pass 

    elif difference == 1:
        new_streak += 1
        print("Streak increased! Keep going!")

    else:
        new_streak = 1
        print("Streak reset. Start again!")

    return new_streak, today_str