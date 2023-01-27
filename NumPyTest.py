import numpy as np
a=np.ones((3,3))
b=np.zeros((3, 3))
x=np.row_stack((a,b))
y=np.ones(x.shape)
print(x)




"""
import cv2
img = cv2.imread('task2.jpg')
cv2.imshow('task',img)
#cv2.waitKey(0)
img2=img.ravel()
#for x in range(len(img2)):
#    for y in range(len(img2[x])):
#        for z in range(len(img2[x][y])):
#            img2[x][y][z] -= 70
#            if img2[x][y][z]<0 : img2[x][y][z]=0
for x in range(len(img2)):
    if img2[x]>100: img2[x]-=100
    else:img2[x]=0
img2=img2.reshape(300,300,3)
print(img2[0])
cv2.imshow('task2', img2)
cv2.waitKey(0)
"""