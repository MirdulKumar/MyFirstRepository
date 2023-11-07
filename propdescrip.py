#!/bin/python3

import sys
import os



# Add Celsius class implementation below.

class Celsius:
    def __get__(self, instance, owner):
        return 5 * (instance.fahrenheit - 32) / 9
    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 5
        # Add temperature class implementation below.        
class Temperature:
    celsius = Celsius()
    def __init__(self, initial_f):
        self.fahrenheit = initial_f

# Add temperature class implementation below.        

    
        
        
'''Check the Tail section for input/output'''

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        t1 = Temperature(int(input()))
        res_lst.append((t1.fahrenheit, t1.celsius))
        t1.celsius = int(input())
        res_lst.append((t1.fahrenheit, t1.celsius))
        fout.write("{}\n{}".format(*res_lst))