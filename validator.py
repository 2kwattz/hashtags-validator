# Hashtags Validator

print("Press 1 to create a list")

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

hashtagsValidator()
