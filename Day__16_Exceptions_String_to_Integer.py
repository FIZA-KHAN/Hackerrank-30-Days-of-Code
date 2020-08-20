#!/bin/python3

import sys


S = input().strip()

try:
    conv = int(S)
    print(conv)
except:
    print("Bad String")
