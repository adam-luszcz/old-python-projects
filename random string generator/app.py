import random
import string


def random_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def random_suffix(value=1):
    if random.randint(0, 1) or value == 1:
        return random_suffix(value * random.randint(2, 9999))
    else:
        return str(value)


print(random_string(7) + random_suffix())

