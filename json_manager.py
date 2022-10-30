"""This module will contain the functionalities to store and load the data from the database json file"""
import hashlib
import json
import os
from pathlib import Path

# class for json file
class JsonManager:
    def __init__(self, file):
        self.file = file
        self.data = []
        self.load()

    # function to load the data from the json file
    def load(self):
        with open(self.file, "r", encoding='utf-8', newline="") as f:
            self.data = json.load(f)
        return self.data

    # function to store the data into the json file
    def store(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
            
    def add_item(self, item):
        self.load()
        self.data.append(item.__dict__)
        self.store(self.data)
