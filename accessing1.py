import cv2
path="flower.jpg"
image=cv2.imread(path)
print('image array dimension: ', image.shape)
print('a pixel: ', image[5,5])
new_image = image[:10,:10]
B = new_image[:,:,0]
G = new_image[:,:,1]
R = new_image[:,:,2]
print('Blue Channel')
print(B)
print('Green Channel')
print(G)
print('Red Channel')
print(R)
