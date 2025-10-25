import json, pygame, sys


def load_data():
    try:
        with open('save_data.json', 'r') as file:
            data = json.load(file)
            return data.get('chips', 1000)
    except (FileNotFoundError, json.JSONDecodeError):
        return 1000

def save_data(chips):
    with open('save_data.json', 'w') as file:
        json.dump({'chips': chips}, file)

def win_chips(amount):
    global chip_count
    chip_count += amount
    save_data(chip_count)

def lose_chips(amount):
    global chip_count
    chip_count = max(0, chip_count - amount)
    save_data(chip_count)

chip_count = load_data()
