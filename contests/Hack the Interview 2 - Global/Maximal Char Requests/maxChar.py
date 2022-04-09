#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxCharCount' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#

def getMaxCharCount(s, queries):
  # queries is a n x 2 array where queries[i][0] and queries[i][1] represents x[i] and y[i] for the ith query.
  result = []
  for q in queries:
    smallestChar = ''
    maxCharNum = -1
    charHash = {}
    for i in range(q[0], q[1] + 1):
      curChar = s[i]
      if s[i].isupper():
        curChar = curChar.lower()
      if ord(curChar) > maxCharNum:
        maxCharNum = ord(curChar)
        smallestChar = curChar
      # add to hash
      if curChar in charHash:
        charHash[curChar] += 1
      else:
        charHash[curChar] = 1
    result.append(charHash[smallestChar])
  return result
    

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  s = input()

  q = int(input().strip())

  query = []

  for _ in range(q):
    query.append(list(map(int, input().rstrip().split())))

  ans = getMaxCharCount(s, query)

  fptr.write('\n'.join(map(str, ans)))
  fptr.write('\n')

  fptr.close()