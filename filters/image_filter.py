import cv2
import numpy as np


def process_image(image_path: str):
    # 1. Load the original RGB/BGR image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not open or find the image: {image_path}")

    # 2. Convert RGB/BGR to Grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Minute Edit: Adjust Brightness & Contrast on RGB image
    # alpha = contrast (1.0-3.0), beta = brightness (0-100)
    enhanced_rgb = cv2.convertScaleAbs(img, alpha=1.2, beta=25)

    # 4. Apply Gaussian Blur Filter (smooths noise)
    blurred_img = cv2.GaussianBlur(img, (7, 7), 0)

    # 5. Apply Canny Edge Detection Filter on Grayscale image
    edges_img = cv2.Canny(gray_img, threshold1=100, threshold2=200)

    # Save all processed images
    cv2.imwrite("output_grayscale.jpg", gray_img)
    cv2.imwrite("output_enhanced_rgb.jpg", enhanced_rgb)
    cv2.imwrite("output_blurred.jpg", blurred_img)
    cv2.imwrite("output_edges.jpg", edges_img)
    print("Image processing complete! Saved 4 edited images.")


if __name__ == "__main__":
    # Replace 'sample.jpg' with your image filename
    process_image(r"C:\Users\54179\OneDrive\Desktop\ankita\GitHub\digital-image-processing\image.jpg")
