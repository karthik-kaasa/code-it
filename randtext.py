from random import randint

"""
Generates random text of given length.
This module make use of random lib for random integer and 
generate random text using selected ASCII/Unicode ordinals.
"""

_Ustart = 65
_Uend = 90
_Sstart = 97
_Send = 122
_Dstart = 48
_Dend = 57

def randtext(len=10):
    """
    Return random text for given len (default=10)
    """
    s = ""
    for i in range(len):
        s += (chr(randint(_Ustart,_Uend)),
        chr(randint(_Sstart,_Send)),
        chr(randint(_Dstart,_Dend)))[randint(0,2)]
    return s

def testsuite():
    print("default len(10):", randtext())
    text = randtext(100)
    print("[len:", len(text), "] ", text, sep="")
    for i in (1000, 10000, 100000, 1000000):
        text = randtext(i)
        print("[len:", len(text), "] ", text[:20], "...", text[-20:], sep="")

if __name__ == "__main__":
   testsuite()

"""
output:
default len(10): Y2x582tCub
[len:100] uZ3qiW5eD0jSnVm6W047CfA7A53eTHT4DLDfFSt6Q9kvfbfeiDKF483BE3I3c99Hl5bvscKBhNHRc04s7nQpKqUyk33S84hg8c88
[len:1000] Vrsx4J0zE2XJp7ET030w...b4a561veh07BzEAnd35A
[len:10000] CAJFwPvv1nBzCH4wT50G...79cBi6n7m6z9Lp71h14p
[len:100000] 63CclP159Xo8yf0X0sDE...B1nsds1gbsUWdU66qw86
"""


