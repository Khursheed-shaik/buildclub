import cv2
import numpy as np

# Constants
CHECKERBOARD_SIZE = 4
SQUARE_SIZE = 100
VIDEO_DURATION = 10  # Duration in seconds
FPS = 10

# Function to create a 4x4 checkerboard pattern
def create_checkerboard(size, square_size):
    checkerboard = np.zeros((size * square_size, size * square_size, 3), dtype=np.uint8)
    for i in range(size):
        for j in range(size):
            color = 255 if (i + j) % 2 == 0 else 0
            checkerboard[i * square_size:(i + 1) * square_size, j * square_size:(j + 1) * square_size] = [color, color, color]
    return checkerboard

# Create the initial checkerboard
checkerboard = create_checkerboard(CHECKERBOARD_SIZE, SQUARE_SIZE)

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = 'checkerboard_video.avi'
out = cv2.VideoWriter(output_file, fourcc, FPS, (checkerboard.shape[1], checkerboard.shape[0]))

# Create frames with color inversion every second
num_frames = VIDEO_DURATION * FPS

for frame_num in range(num_frames):
    # Determine if the current second is odd or even
    if (frame_num // FPS) % 2 == 0:
        frame = checkerboard
    else:
        frame = cv2.bitwise_not(checkerboard)
    
    # Write the frame to the video file
    out.write(frame)
    
    # Display the resulting frame (optional)
    cv2.imshow('Checkerboard', frame)
    
    # Break the loop if 'q' is pressed (for debugging)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when done
out.release()
cv2.destroyAllWindows()

print(f"Video saved as {output_file}.")
