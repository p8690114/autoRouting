import numpy as np                                                                                                                       
import cv2
import pdb


src = cv2.imread("pc2.jpg", 1) # read input image
#src = cv2.imread("globe.png", 1) # read input image
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # convert to grayscale
blur = cv2.blur(gray, (3, 3)) # blur the image

def change_kernel(val):
    if (val % 2 == 1):
        global glo_n
        glo_n = val
        n_iter_callback()

def change_iteration(val):
    global glo_iter
    glo_iter = val
    n_iter_callback()


def n_iter_callback():

#kernel = np.ones((6,6), np.uint8)
#kernel = np.ones((3,3), np.uint8)
    kernel = np.ones((glo_n,glo_n), np.uint8)
#kernel = np.ones((7,7), np.uint8)
    dilation = cv2.dilate(blur, kernel, iterations = glo_iter)
#dilation = cv2.blur(dilation, (3, 3)) # blur the image
    erosion = cv2.erode(dilation, kernel, iterations = glo_iter)

    ret, thresh = cv2.threshold(erosion, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow('input', src)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Result', thresh)

cv2.namedWindow('input')
glo_n=3
max_n = 9
glo_iter = 10
max_iterations = 20
cv2.createTrackbar('kernel size n X n: <only odd>','input',glo_n,max_n,change_kernel) 
cv2.createTrackbar('iterations:','input',glo_iter,max_iterations,change_iteration) 

n_iter_callback()
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

#cv2.waitKey(0)
'''
ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
# Finding contours for the threshold image
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# create hull array for convex hull points
hull = []

#calculate points for each contour
for i in range(len(contours)):
    #creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))




# create an empty black image
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    cv2.drawContours(drawing, hull, i, color, 1, 8)
cv2.imshow('im', drawing)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
