import cv2
import matplotlib.pyplot as plt 
# Read image 
img = cv2.imread("C:\\Users\\54179\\OneDrive\\Desktop\\ankita\\GitHub\\digital-image-processing\\image.jpg") 
if img is None:
    print("Error: Image not found.") 
else:
    blue, green, red = cv2.split(img) 
    plt.figure(figsize=(12, 4)) 
    plt.subplot(1, 3, 1) 
    plt.imshow(red, cmap="gray") 
    plt.title("Red Plane") 
    plt.axis("off")
    plt.subplot(1, 3, 2) 
    plt.imshow(green, cmap="gray")
    plt.title("Green Plane")
    plt.axis("off")
    plt.subplot(1, 3, 3)
    plt.imshow(blue, cmap="gray")
    plt.title("Blue Plane")
    plt.axis("off")
    plt.show()