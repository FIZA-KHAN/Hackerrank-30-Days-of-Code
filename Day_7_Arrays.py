#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in arr[::-1]:
        print(i, end=" ")

    #a = arr[::-1]
    #print(a)