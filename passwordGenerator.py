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
import argparse

args = argparse.ArgumentParser()
args.add_argument('-l', '--length', type=int, default=10)

args = args.parse_args()
vocab = string.ascii_letters + string.digits + string.punctuation


def generate(length):
    password = ''.join(choice(vocab) for i in range(length))
    return password


length = args.length

print(generate(length))
