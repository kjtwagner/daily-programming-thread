#!/usr/bin/env python3

import numpy as np

char_count = 0
text = input("Enter some text to get character count: ")

## take input and find the num char
for i in text:
    char_count += 1
words = text.split(" ")
word_count = len(words)
## return the num and print it for the user
print("Char count: %i" % char_count)
print("Word count: %i" % word_count)
