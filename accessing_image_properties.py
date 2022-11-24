import cv2

# read image
img = cv2.imread(r'road.jpg', 1)

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
size1 = img.size

print('Image Dimensions')
print('================')
print('Image Height       : ', height)
print('Image Width        : ', width)
print('Number of Channels : ', channels)
print('Image Size  :', size1)