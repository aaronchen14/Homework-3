# Use OpenCV to do a bilateral filter to an image, modify from question6.py, you may use your favorite image,
# visualize the images before and after the filtering using matplotlib.

import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Read the image.
img = cv2.imread('Cat_Yelled_At.jpg')

# Apply bilateral filter
# cv2.bilateralFilter ( src, dst, d, sigmaColor,sigmaSpace, borderType = BORDER_DEFAULT )
bilateral = cv2.bilateralFilter(img, 15, 80, 80)
# cv2.imshow('Oringinal', img)
# cv2.imshow('Filter', bilateral)
# cv2.waitKey(0)


plt.figure("Original")
plt.imshow(img)
plt.show()

# I had to close my first figure to see my second one.
plt.figure("Bilateral Filter")
plt.imshow(bilateral)
plt.show()

# Save the output.
cv2.imwrite('bilateral.jpg', bilateral)
