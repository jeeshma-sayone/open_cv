# Importing the OpenCV library
import cv2

# using imread('path') and 0 denotes read as  grayscale image
image = cv2.imread('road.jpg', 1)
# Extracting the height and width of an image
h, w = image.shape[:2]

# Calculating the ratio
ratio = 800 / w

# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)

# Displaying the height and width
print("Height = {}, Width = {}".format(h, w))

# save image
status = cv2.imwrite(r'new_road.jpeg', resize_aspect)
print("Image written to file-system : ", status)

# This is using for display the image
cv2.imshow('image', resize_aspect)

cv2.waitKey(0)  # This is necessary to be required so that the image doesn't close immediately.
# It will run continuously until the key press.
cv2.destroyAllWindows()

