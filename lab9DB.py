import pymongo
import os
import time

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["accounts"]
collection = db["user_profiles"]

def showData():
    foundData = collection.find({}, {"_id": 0, "Username": 1, "Email": 1, "Age": 1})
    for document in foundData:
        print(document)

def insertData():
    newUsername = input("Enter your username: ")
    newEmail = input("Enter your email: ")
    newAge = int(input("Enter your age: "))
    newData = {"Username": newUsername, "Email": newEmail, "Age": newAge}
    collection.insert_one(newData)

def updateData():
    username = input("Enter your username: ")
    prop = input("Enter the property you want to change: ")
    if prop == "Age":
        value = int(input("Enter a new value: "))
    else:
        value = input("Enter a new value: ")

    try:
        collection.find_one_and_update({"Username": username}, {"$set": {prop: value}})
    except:
        print("Username or property or value was wrong, try again!")

def deleteData():
    username = input("Enter your username to delete your profile: ")

    try:
        collection.find_one_and_delete({"Username": username})
    except:
        print("Username was wrong, try again!")

def main():
    while 1:
        print("\nEnter the number of operation you have to do: ")
        print("1) Show Profile\n2) Create Profile\n3) Update Profile\n4) Delete Profile\n5) Exit")
        ch = int(input("Choice: "))
        match ch:
            case 1:
                os.system("cls")
                showData()
            case 2:
                os.system("cls")
                insertData()
                os.system("cls")
            case 3: 
                os.system("cls")
                updateData()
                os.system("cls")
            case 4: 
                os.system("cls")
                deleteData()
                os.system("cls")
            case 5:
                os.system("cls")
                print("See you later")
                print(":)")
                time.sleep(1)
                os.system("cls")
                break
            case _:
                os.system("cls")
                print("Enter your choice more wisely")

    client.close()

main()
