#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    n = bin(n).replace("0b", "")
    n1 = list((n))
    
    #n1 = int(n,2) #converts binary to decimal
    #print(n1)
    ones = 0
    maxOnes = 0
    for i in n1:
        if i == '1':
            ones = ones + 1
        else:
            ones = 0 

        if maxOnes < ones:
            maxOnes = ones
    print(maxOnes)
