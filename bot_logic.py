import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emojis():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

def flip_coin_f():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Heads"
    else:
        return "Tails"
