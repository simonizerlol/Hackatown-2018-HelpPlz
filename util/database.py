from pymongo import MongoClient

class Database():
    def __init__(self):
        self.client = MongoClient(
            'mongodb://hackatown2018HelpPlz:helpplz2018@ds263707.mlab.com:63707/help_plz')
        self.db = self.client.help_plz

    

