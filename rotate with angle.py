# Importing OpenCV Library
import cv2
# Relative or absolute path of the input image file
path = "flower.jpg"
# reading image (by default the flag is 1 if not specidied)
image = cv2.imread(path)
size = image.shape
width = size[0]
height = size[1]
center = (int(height/2),int(width/2))
M = cv2.getRotationMatrix2D(center, 45, 1)
imageRot = cv2.warpAffine(image, M, (height, width))
# Display image in a window
cv2.imshow("Output",image)
cv2.imshow("Rotate",imageRot)
# Wait until any key press (press any key to close the window)
cv2.waitKey()
# kill all the windows
cv2.destroyAllWindows()