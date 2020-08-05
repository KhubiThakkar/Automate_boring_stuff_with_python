#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary =[]
    while n != 1:
        r = n%2
        n = math.floor(n/2)
        binary.append(r)
    binary.append(n)
    print(binary)
    i = 0
    maxi = 0
    for num in range(len(binary)):
        if binary[num] == 1:
            i += 1
            if i > maxi:
                maxi = i
        else:
            i = 0
        
    print(maxi)