import random, string

while True:
    try:

        length = int(input("How many characters you wish on your password: "))

    except:

        print("You need to type numbers only.")

    else:

        chars = string.ascii_letters + string.digits + '!ç@#$%*()-=+_,.;:\/|{}[]~'

        rnd = random.SystemRandom()

        print("".join(rnd.choice(chars) for i in range (length)))

        break