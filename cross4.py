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
    # Now solve for y -- use either line, because they are equal here
    # y = mx + b
    y = m1 * x + b1
    return x,y


#line A
A1 = [1,1]
A2 = [10,10]
#line B
B1 = [18,10]
B2 = [3,6]
slope_A = slope(A1, A2)
print("slope_A {:.2f}".format(slope_A))
slope_B = slope(B1, B2)
print("slope_B {:.2f}".format(slope_B))
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


if (min(A1[0],A2[0]) <= x <= max(A1[0],A2[0])) and (min(A1[1],A2[1]) <= y <= max(A1[1],A2[1])) and \
   (min(B1[0],B2[0]) <= x <= max(B1[0],B2[0])) and (min(B1[1],B2[1]) <= y <= max(B1[1],B2[1])): 
    print("cross at ({:.2f}, {:.2f})".format(x,y))
    #print(line_intersect(slope_A, y_int_A, slope_B, y_int_B))
else:
    print("No cross point !!\n")



import matplotlib.pyplot as plt
plt.plot(X1,Y1,X2,Y2,marker = 'o')
plt.show()
