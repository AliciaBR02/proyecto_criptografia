"""This module will contain the functionalities to store and load the data from the database json file"""
import json
from pathlib import Path

class JsonManager:
    def __init__(self, file):
        self.file = file
        self.data = []
        self.load()

    # load the data from the json file
    def load(self):
        with open(self.file, "r", encoding='utf-8', newline="") as f:
            self.data = json.load(f)
        return self.data

    # store the data into the json file
    def store(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
    
    # update the content of the json file adding an item
    def add_item(self, item):
        self.load()
        self.data.append(item.__dict__)
        self.store(self.data)
