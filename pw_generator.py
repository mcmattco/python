import string
from random import randint


def get_length():
    length = (input("How long should your password be? "))
    while not length.isdigit():
        length = input("NaN, try again dummy.")
    while int(length) < 6:
        length = input("Insecure length, try again, at least 6. ")
        # need to check again for NaN without copying above code
    return int(length)


def pw_complexity():
    global level
    level = int(input("How complex should the password be? (1-5) "))
    if level not in range(1,6):
        level = input("Try again, 1-5 this time. ")
    chars = string.ascii_lowercase
    if level >= 2:   # level 2 is upper and lowercase letters
        chars += string.ascii_uppercase
#    if level >= 3:
#       chars += string.digits
#    if level >= 4:
#        chars += string.punctuation
    if level == 5:
        chars = string.punctuation # oops all special characters!
    return chars


def pw_gen(length, chars):
    pw = ''
    if level < 5: # start pw with a lowercase for all levels except 5
        pw += string.ascii_lowercase[randint(1, len(string.ascii_lowercase))]
        length -= 1
    if level == 3:   # level 3 should include some nums
        x = round(int(length)/3)
        while x > 0:
            pw += string.digits[randint(1, len(string.digits))]
            length -= 1
            x -= 1
    if level == 4:   # level 4 should include 1 special chara and 1 num
        pw += string.punctuation[randint(1, len(string.punctuation))]
        pw += string.digits[randint(1, len(string.digits))]
        length -= 2
    while length > 0:
        pw += chars[randint(1, len(chars))]
        length -= 1
    #TODO: shuffle, keeping first chara a lowercase letter
    return pw

length = get_length()
chars = pw_complexity()
pw = pw_gen(length,chars)
print(pw)
