from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt
# Read image
img = Image.open("C:\\Users\\54179\\OneDrive\\Desktop\\ankita\\GitHub\\digital-image-processing\image.jpg").convert("RGB")
img_array = np.array(img)
horizontal_flip = np.fliplr(img_array)
vertical_flip = np.flipud(img_array)
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(horizontal_flip)
plt.title("Horizontal Flip")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(vertical_flip)
plt.title("Vertical Flip")
plt.axis("off")
plt.show()