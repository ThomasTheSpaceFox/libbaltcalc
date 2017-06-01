#!/usr/bin/env python
import libbaltcalc
from libbaltcalc import btint 
#you can pass a string with balanced ternary integers and even a btint instance.
int1=btint("+-")
int2=btint("+-")
#seamless balanced ternary integer mathematics makes coding easier and more clean.
print int1 + int2
print int1
print int2
#mathematics operations return btint instances.
int3=( - int1)
print int3
print abs(int3)
#the int() method is also supported.
print int(int3)
print "div"
print (int1 / int2)
print ((int1 + int2) / int2)

#you can also pass decimal integers
print btint(585)
print btint(-585)