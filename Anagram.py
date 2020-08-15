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
        for c in s1:
            if not c in s2:
               changes += 1
            else:
                if s1[c] != s2[c]:
                    changes += 1
    return changes

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)