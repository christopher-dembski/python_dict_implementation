import timeit
import random
import string
from collections import OrderedDict


def random_string(length=25):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def make_dict(size):
    return {random_string(): random_string() for _ in range(size)}


def make_ordered_dict(size):
    return OrderedDict(make_dict(size))


def delete_key(d, random_key):
    del d[random_key]


def main():

    for power in range(1, 7):
        print(f'Time to create dict: size={10 ** power}')
        print(timeit.timeit(lambda: make_dict(10 ** power), number=1))

    for power in range(1, 8):
        print(f'Del key from dict: size={10 ** power}')
        d = make_dict(10 ** power)
        random_key = random.choice([key for key in d.keys()])
        print(timeit.timeit(lambda: delete_key(d, random_key), number=1), end='\n')

    for power in range(1, 7):
        print(f'Time to create ordered dict: size={10 ** power}')
        print(timeit.timeit(lambda: make_ordered_dict(10 ** power), number=1))

    for power in range(1, 7):
        print(f'Del key from ordered dict: size={10 ** power}')
        d = make_ordered_dict(10 ** power)
        random_key = random.choice([key for key in d.keys()])
        print(timeit.timeit(lambda: delete_key(d, random_key), number=1), end='\n')


if __name__ == '__main__':
    main()


# # # Results # # #

# result: del appears to be O(1) for Python dict and OrderedDict

# OrderedDict: uses doubly linked list

# Pyton dict?
