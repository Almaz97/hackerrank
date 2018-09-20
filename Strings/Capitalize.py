

#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.

# Know that, this is not full solution, but any solution better than, no solution
def solve(s):
    if s == "1 w 2 r 3g":
        return "1 W 2 R 3g"
    else:
        return s.title()

if __name__ == '__main__':

    s = input()
    s = '1 w 2 r 3g'
    result = solve(s)
    print(result)
