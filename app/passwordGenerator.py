"""
passwordGenerator.py
Isaac Frank
Copyright (C) 2020 Isaac Frank
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

import string
from random import choice
# import argparse

# args = argparse.ArgumentParser()
# args.add_argument('-l', '--length', type=int, default=10)

# args = args.parse_args()


def generate(data):
    vocab = ""
    if data["uppercase"] == 'true':
        vocab += string.ascii_uppercase
    if data["lowercase"] == 'true':
        vocab += string.ascii_lowercase
    if data["numbers"] == 'true':
        vocab += string.digits
    if data["symbols"] == 'true':
        vocab += string.punctuation
    length = int(data["length"])
    if vocab == "":
        password = ''
        return password
    else:
        password = ''.join(choice(vocab) for i in range(length))
        return password
