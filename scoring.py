def calculate_daily_score(daily_record, current_streak):

    score = 0
    
    score += daily_record.get("prayers_done", 0) * 100
    
    score += daily_record.get("quran_done", 0) * 70
    
    score += daily_record.get("dhikr_done", 0) * 20
    
    if daily_record.get("fasted", False):
        score += 200
        
    score += daily_record.get("helping_done", 0) * 50

    bonus_multiplier = 1 + (current_streak * 0.1)
    bonus_multiplier_int = int(bonus_multiplier)
    
    total_points = int(score * bonus_multiplier)
    
    print(f"\nBase Points: {score}")
    print(f"Streak Bonus: {bonus_multiplier_int}")
    print(f"Total Points Today: +{total_points}")

    return total_points