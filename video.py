# import required libraries here
import cv2
# video capture object where 0 is the camera number for a usb camera (orwebcam)
# if 0 doesn't work, you might need to change the camera number to get theright camera you want to access
cam = cv2.VideoCapture(0)
# # for video file, use:
# cam = cv2.VideoCapture('video_file_path')
# # for IP camera, use:
# cam = cv2.VideoCapture('IP_Address')
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)) # convert to integer
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cam.get(cv2.CAP_PROP_FPS)
output_file = 'videos.MP4' # file location + name
output = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'XVID'), fps,
(width, height))
while True:
 _ , frame = cam.read() # reading one frame from the camera object
 cv2.imshow('Webcam', frame) # display the current frame in a windownamed 'Webcam'
 output.write(frame)
 # Waits for 1ms and check for the pressed key
 if cv2.waitKey(1) & 0xff == ord('q'): # press q to quit the camera (getout of the loop)
  break
cam.release() # close the camera
output.release() # close video writer
cv2.destroyAllWindows() # Close all the active windows