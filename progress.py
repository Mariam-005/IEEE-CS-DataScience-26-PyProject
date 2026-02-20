def show_progress(user_data):
    goals = user_data.get("goals", {})
    done = user_data.get("daily_record", {})
    
    print("\n=== DAILY PROGRESS DASHBOARD ===")
    
    target_quran = goals.get("quran_pages", 1) 
    actual_quran = done.get("quran_done", 0)
    if target_quran > 0:
        percent = (actual_quran / target_quran) * 100
        print(f" Quran: {actual_quran}/{target_quran} pages ({percent:.1f}%)")
    
    target_dhikr = goals.get("dhikr_count", 1)
    actual_dhikr = done.get("dhikr_done", 0)
    if target_dhikr > 0:
        percent = (actual_dhikr / target_dhikr) * 100
        print(f" Dhikr: {actual_dhikr}/{target_dhikr} ({percent:.1f}%)")

    actual_prayers = done.get("prayers_done", 0)
    print(f" Prayers: {actual_prayers}/5")

    print("---------------------------------------")
    print(f" Total Score: {user_data.get('total_score', 0)}")
    print(f" Current Streak: {user_data.get('streak', 0)}")
    print("=======================================\n")    