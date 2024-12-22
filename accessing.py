import cv2
import numpy as np
path="flower.jpg"
image=cv2.imread(path)
image[:,:]=(0,0,0)
cv2.imwrite("output.jpg",image)
