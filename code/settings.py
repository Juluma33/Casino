import json

def update_data(**kwargs):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    data.update(kwargs)
    
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def load_width():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            return data.get('Window_Width', 1280)
    except (FileNotFoundError, json.JSONDecodeError):
        return 1280

def load_height():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            return data.get('Window_Height', 720)
    except (FileNotFoundError, json.JSONDecodeError):
        return 720

Window_Height, Window_Width = load_height(), load_width()
