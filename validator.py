# Hashtags Validator
import keyboard
import datetime


# f = open("myfile.txt", "x")

def hashtagsValidator():
    hashtagCollection = []

    while True:
        print("Enter Hashtags")
        hashtagInput = input("Enter a hashtag: ")

        if hashtagInput in hashtagCollection:
            print("Already Present")
        else:
            hashtagCollection.append(hashtagInput)
            print(hashtagCollection)
            print("To Stop Entering, Press Ctrl + C")
  
        dt = datetime.datetime.now().strftime("%Y_%m_%H")
        f = open(f"hashtagsList.txt-{dt}", "a")
        f.write(" ".join(hashtagCollection) + "\n")

   
hashtagsValidator()
