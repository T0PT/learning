import cv2
import numpy as np
def resize(inp, po_x=1, po_y=1):
    size=[po_y*inp.shape[0], po_x*inp.shape[1]]
    out=cv2.resize(inp,size)
    return out
def shift(inp, down=0,right=0):
    out=np.zeros(inp.shape)
    zer=np.array([0,0,0])
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if y>=down and x>=right:out[y][x]=inp[y-down][x-right]
            else: out[y][x]=zer
    return out
def cut(inp,fr_x=0,fr_y=0,to_x=1,to_y=1):
    out = np.zeros([to_x-fr_x,to_y-fr_y,inp.shape[2]])
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if x<=to_x and x>=fr_x and y<=to_y and y>=fr_y:
                out[y-fr_y-1][x-fr_x-1]=inp[y][x]
    return out
img = cv2.imread('test_img_300x300.png')
img2=img
#img2=np.zeros(img.shape)
#for x in range(len(img)):
#    for y in range(len(img[x])):
#        m=int(img[x][y][0])+int(img[x][y][1])+int(img[x][y][2])
#        m=int(m/3)
#        for z in range(len(img[x][y])):
#            img2[x][y][z]=int(m)
#img2.dtype=int
img2=img2/255
cv2.imshow('img',img2)
img2=resize(img2,2,2)
img2=shift(img2,100,100)
cv2.imshow('img2',img2)
img3=cut(img2,50,50,250,250)
cv2.imshow('img3',img3)
cv2.waitKey(0)

"""
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