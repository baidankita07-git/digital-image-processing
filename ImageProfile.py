import cv2
import matplotlib.pyplot as plt
# Read image 
img = cv2.imread("C:\\Users\\54179\\OneDrive\\Desktop\\ankita\\GitHub\\digital-image-processing\\image.jpg") 
if img is None: 
    print("Error: Image not found.") 
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    row = gray[gray.shape[0] // 2, :] 
    plt.figure(figsize=(10, 7)) 
    plt.subplot(2, 1, 1) 
    plt.imshow(gray, cmap="gray") 
    plt.title("Grayscale Image") 
    plt.axis("off")
    plt.subplot(2, 1, 2) 
    plt.plot(row) 
    plt.title("Image Intensity Profile") 
    plt.xlabel("Pixel Position") 
    plt.ylabel("Inte    nsity") 
    plt.grid()
    plt.show()    