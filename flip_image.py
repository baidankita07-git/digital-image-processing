from PIL import Image import numpy as np import matplotlib.pyplot as plt

# Read image

img = Image.open("image.jpg").convert("RGB")

# Convert image to NumPy array img_array = np.array(img)

# Horizontal flip horizontal_flip = np.fliplr(img_array)

# Vertical flip vertical_flip = np.flipud(img_array)

# Display images plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)

plt.imshow(img_array)

plt.title("Original Image")

plt.axis("off")

plt.subplot(1, 3, 2)

plt.imshow(horizontal_flip)

plt.title("Horizontal Flip")

plt.axis("off")

plt.subplot(1, 3, 3) plt.imshow(vertical_flip)

plt.title("Vertical Flip")

plt.axis("off")

plt.show()