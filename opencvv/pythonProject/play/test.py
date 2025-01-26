import cv2
import numpy as np

# Create a blank image (black background)
image = 255 * np.ones((500, 500, 3), dtype=np.uint8)

# Define rectangle coordinates (x, y, width, height)
start_point = (100, 100)
end_point = (300, 200)
color = (0, 255, 0)  # Green
thickness = 2

# Draw the rectangle
cv2.rectangle(image, start_point, end_point, color, thickness)

# Define the name to add
name = "Rectangle 1"

# Calculate the text position
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
font_thickness = 1
text_size = cv2.getTextSize(name, font, font_scale, font_thickness)[0]
text_x = start_point[0] + (end_point[0] - start_point[0] - text_size[0]) // 2
text_y = start_point[1] - 10  # Above the rectangle

# Add the name
cv2.putText(image, name, (text_x, text_y), font, font_scale, color, font_thickness)

# Display the image
cv2.imshow('Image with Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
