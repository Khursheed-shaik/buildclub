# importing required libraries
import cv2
import numpy as np
p1 = (0,0) # top left cornor point
# Mouse callback function
def mouseClick(event,xPos,yPos,flags,param):
 global dp1
 # left click press event
 if event==cv2.EVENT_LBUTTONDOWN:
  p1 = (xPos,yPos)
  print(p1)
# reading image
path = "flower.jpg"
frame = cv2.imread(path)
# Creating an window to display image/frame
cv2.namedWindow('FRAME')
# This function detects every new events and triggers th
cv2.setMouseCallback('FRAME',mouseClick)
while True:
 cv2.imshow('FRAME',frame)
 if cv2.waitKey(1) & 0xff == ord('q'): # to quit press 'q'
  break
cv2.destroyAllWindows()