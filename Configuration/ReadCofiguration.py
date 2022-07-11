import json
import os

_dirname = os.path.dirname(__file__)

class readJson:

    @staticmethod
    def readJsonFile():        
        try:
            with open("/home/dantodsn/data.json") as file:
                data = json.load(file)
                return data
        except:
            with open(_dirname+"/Configuration/default.json") as file:
                data = json.load(file)
                return data