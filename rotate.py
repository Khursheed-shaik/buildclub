# Importing OpenCV Library
import cv2
# Relative or absolute path of the input image file
path ="flower.jpg"
# reading image (by default the flag is 1 if not specidied)
image = cv2.imread(path)
imageRot = cv2.rotate(image, cv2.ROTATE_180)
# Display image in a window
cv2.imshow("Output",image)
cv2.imshow("Resize",imageRot)
# Wait until any key press (press any key to close the window)
cv2.waitKey()
# kill all the windows
cv2.destroyAllWindows()
#