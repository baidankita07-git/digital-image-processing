import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
# Given 2-D data 
data = np.array([
 [0, 50, 100, 150, 200, 255], 
 [50, 100, 150, 200, 255, 200], 
 [100, 150, 200, 255, 200, 150], 
 [150, 200, 255, 200, 150, 100], 
 [200, 255, 200, 150, 100, 50], 
 [255, 200, 150, 100, 50, 0] 
], dtype=np.uint8) 
# Write 2-D data to an image file 
cv2.imwrite("two_d_data.png", data) 
# Read the created image 
saved_image = cv2.imread("two_d_data.png", cv2.IMREAD_GRAYSCALE) 
# Display the image 
plt.figure(figsize=(5, 5)) 
plt.imshow(saved_image, cmap="gray") 
plt.title("Image Created from 2-D Data") 
plt.axis("oƯ")
plt.show()print("2-D data successfully written to 'two_d_data.png'")