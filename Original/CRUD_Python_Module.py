# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, user, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = user 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    def find_next_rec_num(self):
        # get cursor of the animal with the highest rec_num in the database
        cursor = self.database.animals.find().sort({'rec_num':-1}).limit(1);
        # convert cursor to a dict
        last_animal = next(cursor, None)
        if last_animal is None:
            raise Exception("rec_num not found")
        return last_animal['rec_num'] + 1
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is None:
            raise Exception("Nothing to save, because data parameter is empty")
        if not isinstance(data, dict):
            raise Exception("Creation failed because data parameter is not a dictionary")
        data.update({'rec_num': self.find_next_rec_num()}) # add incremented rec_num to dict
        if self.database.animals.insert_one(data): # data should be dictionary
            return True              
        return False # return false if insert failed

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is None:
            return list()
        elif not isinstance(data, dict):
            return list()
        else:
            return list(self.database.animals.find(data)) # data should be dictionary
        
    # Update method to implement the U in CRUD.
    def update(self, data, newData):
        if not isinstance(data, dict):
            raise Exception("Update failed because data parameter is not a dictionary")
        if not isinstance(newData, dict):
            raise Exception("Update failed because newData parameter is not a dictionary")
        result = self.database.animals.update_many(data, newData)
        return result.modified_count
    
    # Delete method to implement the D in CRUD.
    def delete(self, data):
        if data is None:
            raise Exception("Nothing to delete, because data parameter is empty")
        if not isinstance(data, dict):
            raise Exception("Deletion failed because data parameter is not a dictionary")
        result = self.database.animals.delete_many(data)
        return result.deleted_count
