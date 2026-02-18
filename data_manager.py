import json
import os

DB_File = "Tiny_Believer_data.json"

def set_data(data):
  
    try:
        with open(DB_File, "w", encoding="utf-8") as f:
          json.dump(data, f, indent=4, ensure_ascii=False)
        return True 
    except Exception as e:
        print(f"Error happened while saving  {e}")
        return False

def get_data():
    if not os.path.exists(DB_File):
        return {"users": {}}
    
    try:
        with open(DB_File, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"users": {}}
 
