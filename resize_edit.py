from PIL import Image
import matplotlib.pyplot as plt


image_path = r"C:\Users\54179\OneDrive\Desktop\ankita\GitHub\digital-image-processing\image.jpg"  # Replace with your image file path.
new_size = (300, 300)  # Width and height in pixels.

try:
	with Image.open(image_path) as image:
		resized_image = image.resize(new_size)

		plt.imshow(resized_image)
		plt.title(f"Resized image: {new_size[0]} × {new_size[1]}")
		plt.axis("off")
		plt.show()
except FileNotFoundError:
	print(f"Image not found: {image_path}")
except Exception as error:
	print(f"Unable to load or resize the image: {error}")
