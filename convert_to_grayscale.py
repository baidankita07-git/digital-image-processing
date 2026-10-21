import matplotlib.pyplot as plt
from PIL import Image

# Read image
try:
    img = Image.open("C:\\Users\\54179\\OneDrive\\Desktop\\ankita\\GitHub\\digital-image-processing\\image.jpg").convert("RGB")

    # Convert image to grayscale
    gray = img.convert("L")

    # Display grayscale image
    plt.figure(figsize=(6, 5))
    plt.imshow(gray, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")
    plt.show()
except FileNotFoundError:
    print("Error: 'image.jpg' not found.")
