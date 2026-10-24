import cv2
import matplotlib.pyplot as plt
img = cv2.imread("image.jpg", 0)
# Low Pass Filter
low_pass = cv2.GaussianBlur(img, (5, 5), 0)
# High Pass Filter
blur = cv2.GaussianBlur(img, (5, 5), 0)
high_pass = cv2.subtract(img, blur)
plt.figure(figsize=(10, 6))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(low_pass, cmap="gray")
plt.title("Low Pass Filter")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(high_pass, cmap="gray")
plt.title("High Pass Filter")
plt.axis("off")
plt.show()