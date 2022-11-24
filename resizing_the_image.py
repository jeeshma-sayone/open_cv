# Importing the OpenCV library
import cv2

from reading_an_image import h, w

# Reading the image using imread() function
image = cv2.imread('road.jpg')
# # resize() function takes 2 parameters,
# # the image and the dimensions
# resize = cv2.resize(image, (800, 800))


# Calculating the ratio
ratio = 800 / w

# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)

# Extracting the height and width of an image
h, w = resize_aspect.shape[:2]
# Displaying the height and width
print("Height = {}, Width = {}".format(h, w))
