# Python program to explain cv2.cvtColor() method

# importing cv2
import cv2

# path
path = r'road.jpg'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2HSV color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)  # This is necessary to be required so that the image doesn't close immediately.
# It will run continuously until the key press.
cv2.destroyAllWindows()
