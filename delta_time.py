#!/bin/python3

'''import math
import os
import random
import re
import sys'''
import datetime
#from os import times_result

# Complete the time_delta function below.
def time_delta(t1, t2):
    f = '%a %d %b %Y %H:%M:%S %z'
    a = datetime.datetime.strptime(t1, f)
    b = datetime.datetime.strptime(t2,f)
    
    time_result = abs(int((a - b).total_seconds()))
    return str(time_result)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = 1

    for t_itr in range(t):
        t1 = 'Sun 10 May 2015 13:54:36 -0700'

        t2 = 'Sun 10 May 2015 13:54:36 -0000'

        delta = time_delta(t1, t2)

        print(delta + '\n')