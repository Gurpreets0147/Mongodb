
from pprint import pprint
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

# print(os.getenv("DEMO_MONGO_URL"))
client=MongoClient(os.getenv("DEMO_MONGO_URL"),serverSelectionTimeoutMS=10000) #Mongo Client

# try:
#     pprint(client.server_info())           # check database connectivity
# except Exception:
#     print("Unable to connect to the server.")


db=client["Demo"]          # DataBase Name
collection=db["users"]      # Collection Name



# post={"_id":0,"name":"hell"}  
# collection.insert_one(post)   # Inser single record

# post1={"name":"hello"}
# post2={"name":"world"}
# collection.insert_many([post1,post2]) # Inser multiple record

# results=collection.find_one({"name":"hell"}) # It get singe document or if name is multiple in same collection it gets first document with the same name
# print(results)

# results=collection.find({"name":"hello"})  # Get multiple documments which meet the expression
# pprint(list(results))
# for result in results:
#     print(result)

# results=collection.find({})  # Get all documments in the collection
# for result in results:
#     print(result)

# results=collection.delete_one({"_id":0})    # Delete single record
# print(results.deleted_count)

# results=collection.delete_many({"name":"hell"})    # Delete multiple records
# print(results.deleted_count)

# results=collection.delete_many({})    # Delete every record in selected collection
# print(results.deleted_count)

# results= collection.update_one({"name":"hello"},{"$set":{"name":"ho"}})
# print(results.matched_count)
# print(results.modified_count)

# results= collection.update_many({"name":"hello"},{"$set":{"test":{"test":None}}})
# print(results.matched_count)
# print(results.modified_count)

# results=collection.count_documents({"name":"hello"})
# print(results)


# test=db["test"]                     # Insert data in second table
# results=collection.find({})
# for result in results:
#     print(result)
#     test.insert_one(result)