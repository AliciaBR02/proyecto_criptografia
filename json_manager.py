"""This module will contain the functionalities to store and load the data from the database json file"""
import json
from pathlib import Path

class JsonManager:
    def __init__(self, file):
        self.file = file
        self.data = []
        self.load()

    def load(self):
        """Load the data from the json file"""
        with open(self.file, "r", encoding='utf-8', newline="") as f:
            self.data = json.load(f)
        return self.data

    def store(self, data):
        """Store the data in the json file"""
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
    
    def add_item(self, item):
        """Add an item to the json file"""
        self.load()
        self.data.append(item.__dict__)
        self.store(self.data)
