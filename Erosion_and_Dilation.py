import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
img = cv2.imread("image.jpg", 0) 
# Convert to binary 
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
# Structuring element 
kernel = np.ones((5, 5), np.uint8) 
# Erosion 
erosion = cv2.erode(binary, kernel, iterations=1) 
# Dilation 
dilation = cv2.dilate(binary, kernel, iterations=1) 
plt.figure(figsize=(10, 6)) 

plt.subplot(1, 3, 1) 
plt.imshow(binary, cmap="gray") 
plt.title("Binary Image") 
plt.axis("off") 

plt.subplot(1, 3, 2) 
plt.imshow(erosion, cmap="gray") 
plt.title("Erosion") 
plt.axis("off") 

plt.subplot(1, 3, 3) 
plt.imshow(dilation, cmap="gray") 
plt.title("Dilation") 
plt.axis("off") 

plt.show()
