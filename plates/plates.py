## This is the project I made for CS50P: Introduction to Python. This project requires making a program that checks the input 
# against the following conditions of applying for a Vanity Number Plate: 
# All vanity plates must start with at least two letters.
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. 
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def twoLetter(s):
    two_letter= s[0:2]
    if two_letter.isalpha():
        return True
    else:
        return False

def charLimit(s):
    numChar=0
    for i in s:
        numChar+=1
    if 2<=numChar<=6:
        return True
    else:
        return False

def forbiddenPassed(s):
    for i in s:
        if i in [".", ",", " ", "!"]:
            return False
    return True

def numPassed(s):
    index=0
    for i in s:
        index+=1
        if i.isdigit():
            break
    numInBetween= s[index:]
    if i=="0":
        return False
    else:
        for q in numInBetween:
            if q.isalpha():
                return False
    return True

def main():
    plate = input("Plate: ")
    plate= plate.strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if twoLetter(s) and charLimit(s) and forbiddenPassed(s) and numPassed(s):
        return True

main()
