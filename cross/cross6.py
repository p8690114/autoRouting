#$ python3 cross6.py [1,2] [4,2] [1,3] [6,5]
#$ python3 cross6.py [2105,1034] [2217,636] [1917,1081] [2626,770]
#python3 cross6.py  [2326.06,790] [1512,1247] [2105,1034] [2217,636]
import ast
import sys


def slope(P1, P2):
    # dy/dx
    # (y2 - y1) / (x2 - x1)
    return(P2[1] - P1[1]) / (P2[0] - P1[0])

def y_intercept(P1, slope):
    # y = mx + b
    # b = y - mx
    # b = P1[1] - slope * P1[0]
    return P1[1] - slope * P1[0]

def line_intersect(m1, b1, m2, b2):
    if m1 == m2:
        print ("These lines are parallel!!!")
        return None
    # y = mx + b
    # Set both lines equal to find the intersection point in the x direction
    # m1 * x + b1 = m2 * x + b2
    # m1 * x - m2 * x = b2 - b1
    # x * (m1 - m2) = b2 - b1
    # x = (b2 - b1) / (m1 - m2)
    x = (b2 - b1) / (m1 - m2)
    #x = round(x,2)
    x = round(x,6)
    # Now solve for y -- use either line, because they are equal here
    # y = mx + b
    y = m1 * x + b1
    #y = round(y,2)
    y = round(y,6)
    return round(x,2),round(y,2)

A1 = ast.literal_eval(sys.argv[1])
A2 = ast.literal_eval(sys.argv[2])
B1 = ast.literal_eval(sys.argv[3])
B2 = ast.literal_eval(sys.argv[4])

#line A
#A1 = [1,1]
#A2 = [10,10]
#B1 = [5649.08,4708.26]
#B2 = [5533.94,2725.8]
#B1 = [4917.83,3843.23]
#B2 = [4831.0,4015.94]
#line B
#A1 = [5647.0,4156.0]
#A2 = [5611.0,4156.0]
#A1 = [4873.57,3924.14]
#A2 = [4917.9,3924.14]
slope_A = slope(A1, A2)
#print("slope_A {:.2f}".format(slope_A))
#print("slope_A {:.6f}".format(slope_A))
#print("slope_A {}".format(slope_A))
slope_B = slope(B1, B2)
#print("slope_B {:.2f}".format(slope_B))
#print("slope_B {:.6f}".format(slope_B))
#print("slope_B {}".format(slope_B))
y_int_A = y_intercept(A1, slope_A)
y_int_B = y_intercept(B1, slope_B)

x,y=line_intersect(slope_A, y_int_A, slope_B, y_int_B)

#X1 = [A1[0], A2[0]]
#Y1 = [A1[1], A2[1]]
#X2 = [B1[0], B2[0]]
#Y2 = [B1[1], B2[1]]

X1 = [item[0] for item in [A1, A2]]
Y1 = [item[1] for item in [A1, A2]]
X2 = [item[0] for item in [B1, B2]]
Y2 = [item[1] for item in [B1, B2]]

print("A x : {} <= {} <= {}".format(min(A1[0],A2[0]), x , max(A1[0],A2[0])))
print("A y : {} <= {} <= {}".format(min(A1[1],A2[1]), y , max(A1[1],A2[1])))
print("B x : {} <= {} <= {}".format(min(B1[0],B2[0]), x , max(B1[0],B2[0])))
print("B y : {} <= {} <= {}".format(min(B1[1],B2[1]), y , max(B1[1],B2[1])))

if (min(A1[0],A2[0]) <= x <= max(A1[0],A2[0])) and (min(A1[1],A2[1]) <= y <= max(A1[1],A2[1])) and \
   (min(B1[0],B2[0]) <= x <= max(B1[0],B2[0])) and (min(B1[1],B2[1]) <= y <= max(B1[1],B2[1])): 
    print("cross at ({:.2f}, {:.2f})".format(x,y))
    #print("cross at ({:.6f}, {:.6f})".format(x,y))
    #print(line_intersect(slope_A, y_int_A, slope_B, y_int_B))
else:
    print("No cross point !!\n")



import matplotlib.pyplot as plt
plt.plot(X1,Y1,X2,Y2,marker = 'o')
plt.show()
