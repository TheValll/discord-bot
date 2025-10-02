import random

def get_random():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    word = ""
    for i in range(5):
        word+= letters[random.randint(0, 25)]

    return word

if __name__ == "__main__":
    get_random()