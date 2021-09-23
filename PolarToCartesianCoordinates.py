'''
This code proposed two transferring function: polar to Cartesian, as well as Cartesian to polar.
we use x + yj to denote Cartesian coordinate and use (u, v) to denote polar coordinate.

1. polar coordinate to Cartesian coordinate ### (u, v)--->x + yj
x = u*cos(v)
y = u*sin(v) 

2. Cartesian coordinate to polar coordinate ### x + yj--->(u, v)
u = sqrt(x**2 + y**2)
v = arctan2(y/x)
The 'arctan2' means we take Quadrant of Cartesian coordinate into consideration.
Since if we just apply common arctan() function, we will get the wrong result.
acrtan2(y/x) = arctan(y/x) ... if x > 0
acrtan2(y/x) = arctan(y/x) + pi ... if x < 0 and y >= 0
acrtan2(y/x) = arctan(y/x) - pi ... if x < 0 and y < 0
acrtan2(y/x) = 0.5*pi ... if x == 0 and y > 0
acrtan2(y/x) = -0.5*pi ... if x == 0 and y < 0
acrtan2(y/x) = 0 ... if x == 0 and y == 0
Thus the range of arctan2(y/x) is (-pi, pi]
'''
from cmath import *

z1 = 2 + 0.5j # 1st Quadrant
u1, v1 = polar(z1) # function polar() transfer z from Cartesian coordinate to polar coordinate
print('u1 = ',u1,' v1 = ',v1)
num1 = rect(u1, v1) #function rect() transfer (u, v) from polar coordinate to Cartesian coordinate
print('num1 = ',num1)

z2 = -2 + 0.5j # 2nd Quadrant
u2, v2 = polar(z2) # function polar() transfer z from Cartesian coordinate to polar coordinate
print('u2 = ',u2,' v2 = ',v2)
num2 = rect(u2, v2) #function rect() transfer (u, v) from polar coordinate to Cartesian coordinate
print('num2 = ',num2)

z3 = -2 - 0.5j # 3rd Quadrant
u3, v3 = polar(z3) # function polar() transfer z from Cartesian coordinate to polar coordinate
print('u3 = ',u3,' v3 = ',v3)
num3 = rect(u3, v3) #function rect() transfer (u, v) from polar coordinate to Cartesian coordinate
print('num3 = ',num3)

z4 = 2 - 0.5j # 4th Quadrant
u4, v4 = polar(z4) # function polar() transfer z from Cartesian coordinate to polar coordinate
print('u4 = ',u4,' v4 = ',v4)
num4 = rect(u4, v4) #function rect() transfer (u, v) from polar coordinate to Cartesian coordinate
print(num4)