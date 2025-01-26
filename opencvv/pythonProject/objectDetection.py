import cv2
import numpy as np
farm_img=cv2.imread("used/township5.jpg")
cotton_img=cv2.imread("used/township3.jpg")
# Multi-scale matching
threshold = 0.5
scales = np.linspace(0.5, 1.5, 10)  # Scale the template from 50% to 150%
rectangles = []

for scale in scales:
    resized_template = cv2.resize(cotton_img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    result = cv2.matchTemplate(farm_img, resized_template, cv2.TM_CCOEFF_NORMED)
    yloc, xloc = np.where(result >= threshold)

    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(resized_template.shape[1]), int(resized_template.shape[0])])
        rectangles.append(
            [int(x), int(y), int(resized_template.shape[1]), int(resized_template.shape[0])])  # Duplicate for grouping

# Group overlapping rectangles
rectangles, _ = cv2.groupRectangles(rectangles, 1, 0.2)

# Draw rectangles and add labels
for (x, y, w, h) in rectangles:
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.putText(farm_img, "Cotton", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 1)

cv2.imshow("Multi-Scale Matching", farm_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




