#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the anagram function below.
def anagram(s):
    sLen = len(s)
    if sLen % 2 != 0:
        return -1
    else:
        changes = 0
        s1 = Counter(s[:sLen//2])
        s2 = Counter(s[sLen//2:])
        cs = []
        for c in s[:sLen//2]:
            if not c in s2:
                changes += 1
            elif not c in cs:
                diff = s1[c] - s2[c]
                if diff > 0:
                   changes += diff 
                cs.append(c)
    return changes


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)