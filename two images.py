import cv2
import numpy as np

# Paths to the input images
path2 = "bts.jpg"
path1 = "flower.jpg"

# Read the input images
image1 = cv2.imread(path1)
image2 = cv2.imread(path2)

# Check if images have been successfully loaded
if image1 is None or image2 is None:
    print(f"Error: Unable to load one or more images.")
    exit()

# Resize images to the same height (assuming they have different heights)
height = max(image1.shape[1], image2.shape[1])
image1 = cv2.resize(image1, (int(image1.shape[1] * height / image1.shape[0]), height))
image2 = cv2.resize(image2, (int(image2.shape[1] * height / image2.shape[0]), height))

# Concatenate images side-by-side
new_img_color = np.hstack((image1, image2))

# Convert concatenated image to grayscale
new_img_gray = cv2.cvtColor(new_img_color, cv2.COLOR_BGR2GRAY)

# Stack colored pair images on top and gray pair images on the bottom
final_image = np.hstack((new_img_color, cv2.cvtColor(new_img_gray, cv2.COLOR_GRAY2BGR)))

# Save the final image
cv2.imwrite('A1_solution.jpg', final_image)

# Display the final image
cv2.imshow("Final Image",final_image )
cv2.waitKey(0)
cv2.destroyAllWindows()