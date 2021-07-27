#!/usr/bin/env python3

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# init cond
n = 4000000
sum = 2
i, j = 1, 2
ij = 0

# keep the sum under some limit
while ij < n:
    ij = i + j
    # check if the second term is even (e+o=e)
    if ij % 2 == 0:
        sum += ij
    i = j
    j = ij

print(sum)
