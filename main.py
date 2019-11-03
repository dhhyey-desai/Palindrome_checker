import pymongo
from pymongo import MongoClient

data = MongoClient()

db = data.palindrome_checker

users = db.users

while True:
    word = input("Please enter a word\n")

    rev = word[::-1]

    if word == rev:

        print("This word is a palindrome")

        user1 = ({"Palindrome": word})

        user_id = users.insert_one(user1).inserted_id

    else:

        print("This word is not a palindrome")

        user1 = ({"Not a Palindrome": word})

        user_id = users.insert_one(user1).inserted_id

    option = input("Would you like to see more Palindromes?[Y/N]\n")

    if option == "Y":
        words = db.users.find({"Palindrome": word})
        print(words)
        for doc in words:
            print(doc)

    else:
        pass
    pass

