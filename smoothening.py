# Importing OpenCV Library
import cv2
# Relative or absolute path of the input image file
path = "flower.jpg"
# reading image (by default the flag is 1 if not specidied)
image = cv2.imread(path)
median = image.copy()
gaussian = image.copy()
median = cv2.medianBlur(median,7)
gaussian = cv2.GaussianBlur(gaussian, (7, 7), cv2.BORDER_DEFAULT)
# Display image in a window
cv2.imshow("Original",image)
cv2.imshow("Median Blur",median)
cv2.imshow("Gaussian Blur",gaussian)
# Wait until any key press (press any key to close the
cv2.waitKey()
# kill all the windows
cv2.destroyAllWindows()