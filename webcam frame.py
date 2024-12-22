# import required libraries here
import cv2
# video capture object where 0 is the camera number for a usb camera (orwebcam)
# if 0 doesn't work, you might need to change the camera number to get theright camera you want to access
cam = cv2.VideoCapture(0)
# Getting camera feed width and height
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cam.get(cv2.CAP_PROP_FPS)

while True:
 i, frame = cam.read() # reading one frame from the camera object
 cv2.imshow('Webcam', frame) # display the current frame in a windownamed 'Webcam'
 print('resolution:',width, 'x', height, '| frames per second:', fps)
 # Waits for 1ms and check for the pressed key
 if cv2.waitKey(1) & 0xff == ord('q'): # press q to quit the camera (getout of loop)
  break
cam.release() # close the camera
cv2.destroyAllWindows() # Close all the active windows