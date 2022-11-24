# Importing the OpenCV library
import cv2

# Reading the image using imread() function
image = cv2.imread('road.jpg')
# We will calculate the region of interest
# by slicing the pixels of the image
roi = image[100: 500, 200: 700]
print(roi)