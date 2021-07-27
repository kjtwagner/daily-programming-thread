#!/usr/bin/env python3

import numpy as np

# loop through and replace
i = 0
for i in range(1,101):
    # divisible by 3 is Fizz
    if i  % 3 == 0:
        print("Fizz")
        i+=1
    # divisible by 5 is Buzz
    elif i  % 5 == 0:
        print("Buzz")
    # if neither, leave num alone
    else:
        print(i)
        i += 1
