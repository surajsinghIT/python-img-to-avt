import cv2
import numpy as np

# Load the original image
image = cv2.imread("img2.png")

# Apply the cartoon effect to the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
color = cv2.bilateralFilter(image, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Create a circular mask
mask = np.zeros_like(cartoon)
center = (mask.shape[1] // 2, mask.shape[0] // 2)
radius = min(mask.shape[1] // 2, mask.shape[0] // 2)
cv2.circle(mask, center, radius, (255, 255, 255), -1)

# Apply the circular mask to the cartoon image
masked_cartoon = cv2.bitwise_and(cartoon, mask)

# Create the blue circular border
border_color = (255, 0, 0)  # Blue color
border_thickness = 15
cv2.circle(masked_cartoon, center, radius, border_color, border_thickness)

# Calculate the output size to fit the circular border
output_width, output_height = 500, 500  # Adjust the desired medium size as needed
output_size = (output_width, output_height)

# Resize the resulting image to fit the circular border
resized_masked_cartoon = cv2.resize(masked_cartoon, output_size, interpolation=cv2.INTER_AREA)

# Display the resulting image with the circular border
cv2.imshow("Cartoon Image with Circular Border (Medium Size)", resized_masked_cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
