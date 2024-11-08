import string
import time

def brute_force_hello_world():
    #Initialize variables
    target_string = input("Enter a Word or Phrase: ")
    guess = ""
    char = ""
    #Create list of upper and lowercase letters
    alphabetList = list(string.ascii_uppercase + string.ascii_lowercase + " ")
    #Search through target_string
    for i in range(len(target_string)):
        #Search through alphabet
        for char in range(len(alphabetList)):
            #Match letter to indexed letter in target_string
            if alphabetList[char] == target_string[i]:
                guess += alphabetList[char]
                break
            print(guess, alphabetList[char], end="\r")
            #Used to track how long it takes to brute force the string
            time.sleep(0.01)
    print("Complete: " + guess)

brute_force_hello_world()