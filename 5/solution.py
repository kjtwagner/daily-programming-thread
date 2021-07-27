#!/usr/bin/env python3

import numpy as np

# fizz buzz
nums = np.arange(1,101,1)
nums = list(nums)

# loop through and replace
i = 0
for i in range(len(nums)):
    # divisible by 3 is Fizz
    if nums[i] % 3 == 0:
        nums[i] = "Fizz"
        i+=1
    # divisible by 5 is Buzz
    elif nums[i] % 5 == 0:
        nums[i] = "Buzz"
    # if neither, leave num alone
    else:
        i += 1
        
# print final answer
print(nums)

