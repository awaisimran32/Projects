import cv2
import numpy as np

# Initialize rectangles lists and scales
rectangles = []
rectangles2 = []
scales = np.linspace(0.5, 1.5, 10)
threshold = 0.5

# Load images
cotton_img = cv2.imread("used/township3.jpg")
farm_img = cv2.imread("used/township1.jpg")
potato_img = cv2.imread("used/township4.jpg")

# Convert images to grayscale
cotton_img = cv2.cvtColor(cotton_img, cv2.COLOR_BGR2GRAY)
potato_g_img = cv2.cvtColor(potato_img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.cvtColor(farm_img, cv2.COLOR_BGR2GRAY)

# Iterate through scales
for scale in scales:
    resized_template = cv2.resize(cotton_img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    resized_template2 = cv2.resize(potato_g_img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

    # Perform template matching
    result = cv2.matchTemplate(gray_img, resized_template, cv2.TM_CCOEFF_NORMED)
    result2 = cv2.matchTemplate(gray_img, resized_template2, cv2.TM_CCOEFF_NORMED)

    # Find locations where matching exceeds the threshold
    yloc, xloc = np.where(result >= threshold)
    yloc2, xloc2 = np.where(result2 >= threshold)

    # Append rectangles for "Cotton"
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(resized_template.shape[1]), int(resized_template.shape[0])])

    # Append rectangles for "Potato"
    for (x, y) in zip(xloc2, yloc2):
        rectangles2.append([int(x), int(y), int(resized_template2.shape[1]), int(resized_template2.shape[0])])

# Group rectangles
rectangles, weight = cv2.groupRectangles(rectangles, 1, 0.2)
rectangles2, weight2 = cv2.groupRectangles(rectangles2, 1, 0.2)

# Draw and label rectangles on the image
for (x, y, w, h) in rectangles:
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (255, 255, 255), 2)
    label = "Cotton"
    font = cv2.FONT_HERSHEY_TRIPLEX
    font_scale = 0.6
    font_thickness = 1
    text_color = (255, 255, 255)
    text_size = cv2.getTextSize(label, font, font_scale, font_thickness)[0]
    text_x = x
    text_y = y - 10
    if text_y < 0:
        text_y = y + 20
    cv2.putText(farm_img, label, (text_x, text_y), font, font_scale, text_color, font_thickness)

for (x, y, w, h) in rectangles2:
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    label2 = "Potato"
    font2 = cv2.FONT_HERSHEY_TRIPLEX
    font_scale2 = 0.6
    font_thickness2 = 1
    text_color2 = (0, 255, 255)
    text_size2 = cv2.getTextSize(label2, font2, font_scale2, font_thickness2)[0]
    text_x2 = x
    text_y2 = y - 10
    if text_y2 < 0:
        text_y2 = y + 20
    cv2.putText(farm_img, label2, (text_x2, text_y2), font2, font_scale2, text_color2, font_thickness2)

# Display the final image
cv2.imshow("Labeled Image", farm_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
