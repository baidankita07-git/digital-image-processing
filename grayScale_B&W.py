import cv2
import matplotlib.pyplot as plt
# Read image 
img = cv2.imread("C:\\Users\\54179\\OneDrive\\Desktop\\ankita\\GitHub\\digital-image-processing\\image.jpg") 
if img is None: 
    print("Error: 'sample.jpg' not found.") 
else: 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    _, bw = cv2.threshold( 
    gray, 
    127, 
    255, 
    cv2.THRESH_BINARY) 
    plt.figure(figsize=(6, 5)) 
    plt.imshow(bw, cmap="gray") 
    plt.title("Black and White Image") 
    plt.axis("off")
    plt.show()