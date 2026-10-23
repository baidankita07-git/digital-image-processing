import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
img = cv2.imread(r"C:\Users\54179\OneDrive\Desktop\ankita\GitHub\digital-image-processing\image.jpg", 0)
# Salt and Pepper noise 
sp_noise = img.copy()
prob = 0.05 
random = np.random.random(img.shape) 
sp_noise[random < prob/2] = 0 
sp_noise[random > 1 - prob/2] = 255
# Median filter 
median = cv2.medianBlur(sp_noise, 5)
# Gaussian noise 
noise = np.random.normal(0, 25, img.shape) 
gaussian = img.astype(np.float32) + noise 
gaussian = np.clip(gaussian, 0, 255).astype(np.uint8) 
# Gaussian filter 
gaussian_filtered = cv2.GaussianBlur(gaussian, (5, 5), 0) 
plt.figure(figsize=(10, 8)) 
plt.subplot(2, 3, 1) 
plt.imshow(img, cmap="gray") 
plt.title("Original") 
plt.axis("off") 

plt.subplot(2, 3, 2) 
plt.imshow(sp_noise, cmap="gray") 
plt.title("Salt & Pepper Noise") 
plt.axis("off")
 
plt.subplot(2, 3, 3) 
plt.imshow(median, cmap="gray") 
plt.title("Median Filter") 
plt.axis("off") 

plt.subplot(2, 3, 4) 
plt.imshow(gaussian, cmap="gray") 
plt.title("Gaussian Noise") 
plt.axis("off") 

plt.subplot(2, 3, 5) 
plt.imshow(gaussian_filtered, cmap="gray") 
plt.title("Gaussian Filter") 
plt.axis("off") 
plt.show()