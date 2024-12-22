import cv2
import numpy as np

# Global variables
img = None
window_name = 'Simple Photo Editor'
filter_type = 0
zoom_factor = 1.0
angle = 0
blur_kernel_size = 1
edge_threshold1 = 50
edge_threshold2 = 150
crop_x1, crop_y1, crop_x2, crop_y2 = 0, 0, 0, 0
is_cropping = False

# Callback functions
def update_filter(val):
    global filter_type
    filter_type = val

def update_zoom(val):
    global zoom_factor
    zoom_factor = val / 10.0

def update_rotation(val):
    global angle
    angle = val

def update_blur(val):
    global blur_kernel_size
    blur_kernel_size = val * 2 + 1

def update_edge1(val):
    global edge_threshold1
    edge_threshold1 = val

def update_edge2(val):
    global edge_threshold2
    edge_threshold2 = val

def mouse_callback(event, x, y, flags, param):
    global crop_x1, crop_y1, crop_x2, crop_y2, is_cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        crop_x1, crop_y1 = x, y
        is_cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        crop_x2, crop_y2 = x, y
        is_cropping = False

def apply_filter(image, filter_type):
    if filter_type == 1:
        return cv2.applyColorMap(image, cv2.COLORMAP_JET)
    elif filter_type == 2:
        return cv2.applyColorMap(image, cv2.COLORMAP_HOT)
    return image

def main():
    global img, window_name

    # Load image
    img = cv2.imread('flower.jpg')
    if img is None:
        print("Image not found!")
        return

    # Create a window and trackbars
    cv2.namedWindow(window_name)
    cv2.createTrackbar('Filter', window_name, 0, 2, update_filter)
    cv2.createTrackbar('Zoom', window_name, 10, 30, update_zoom)
    cv2.createTrackbar('Rotation', window_name, 0, 360, update_rotation)
    cv2.createTrackbar('Blur', window_name, 0, 10, update_blur)
    cv2.createTrackbar('Edge1', window_name, 50, 255, update_edge1)
    cv2.createTrackbar('Edge2', window_name, 150, 255, update_edge2)

    cv2.setMouseCallback(window_name, mouse_callback)

    while True:
        # Apply filter
        filtered_img = apply_filter(img, filter_type)

        # Zoom
        h, w = filtered_img.shape[:2]
        center = (w // 2, h // 2)
        M_zoom = cv2.getRotationMatrix2D(center, 0, zoom_factor)
        zoomed_img = cv2.warpAffine(filtered_img, M_zoom, (w, h))

        # Rotation
        M_rotate = cv2.getRotationMatrix2D(center, angle, 1)
        rotated_img = cv2.warpAffine(zoomed_img, M_rotate, (w, h))

        # Blurring
        if blur_kernel_size > 1:
            blurred_img = cv2.GaussianBlur(rotated_img, (blur_kernel_size, blur_kernel_size), 0)
        else:
            blurred_img = rotated_img

        # Edge Detection
        gray = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, edge_threshold1, edge_threshold2)
        sketch_img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        # Cropping
        if not is_cropping and crop_x1 and crop_x2 and crop_y1 and crop_y2:
            x1, y1, x2, y2 = min(crop_x1, crop_x2), min(crop_y1, crop_y2), max(crop_x1, crop_x2), max(crop_y1, crop_y2)
            crop_img = sketch_img[y1:y2, x1:x2]
            cv2.imshow('Cropped Image', crop_img)
            cv2.imwrite('cropped_image.jpg', crop_img)
        else:
            crop_img = sketch_img

        cv2.imshow(window_name, crop_img)

        key = cv2.waitKey(1)
        if key == 27:  # Esc key to exit
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
