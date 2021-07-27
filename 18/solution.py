#!/usr/bin/env python3

text = input("Enter some text to get character count: ")

## take input and find the num char
char_count = 0
for i in text: char_count += 1
word_count = len(text.split(" "))

## return the num and print it for the user
print("Char count: %i" % char_count)
print("Word count: %i" % word_count)
