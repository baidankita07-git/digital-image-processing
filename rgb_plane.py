import cv2
import matplotlib.pyplot as plt 
# Read image 
img = cv2.imread("image.jpg") 
if img is None: 
 print("Error: Image not found.") 
else: 
 # OpenCV reads images in BGR format 
 blue, green, red = cv2.split(img) 
 # Display R, G and B planes 
 plt.figure(figsize=(12, 4)) 
 plt.subplot(1, 3, 1) 
 plt.imshow(red, cmap="gray") 
 plt.title("Red Plane") 
 plt.axis("oƯ")
 plt.subplot(1, 3, 2) 
 plt.imshow(green, cmap="gray") 
 plt.title("Green Plane") plt.axis("oƯ")
 plt.subplot(1, 3, 3) 
 plt.imshow(blue, cmap="gray") 
 plt.title("Blue Plane") 
 plt.axis("oƯ")
 plt.show()