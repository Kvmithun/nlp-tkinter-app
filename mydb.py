import json
import os

class Database:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "db.json")
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def add_data(self, name, email, password):
        with open(self.file_path, 'r') as rf:
            database = json.load(rf)

        if email in database:
            return 0
        else:
            database[email] = [name, password]
            with open(self.file_path, 'w') as wf:
                json.dump(database, wf)
            return 1
    def search (self,email,password):
        with open('/Users/mithunkv/Desktop/basic projects/nlp/nlp/db.json','r') as rf:
            database=json.load(rf)
            if email in database:
                if database[email][1]==password:
                    return 1
                else:
                    return 0
            else:
                return 0
