# python program to find the area of the circle for two digit radius.


#defining the constants
pi = 22/7

#defining the limits
import numpy as np

k = np.arange(100)

#defining the variable
r = float(input("ENTER THE RADIUS :: "))

#defining the function
area = pi * r * r

if r in k:
    print(area)
else:
 print("given value is no valid!")
 