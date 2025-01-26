import cv2
import numpy as np


rectangles = []
rectangles2=[]
scales=np.linspace(0.5,1.5,10)
threshold = 0.5



cotton_img = cv2.imread("used/township3.jpg")
farm_img = cv2.imread("used/township5.jpg")
potato_img = cv2.imread("used/township4.jpg")


cotton_img = cv2.cvtColor(cotton_img, cv2.COLOR_BGR2GRAY)
potato_g_img = cv2.cvtColor(potato_img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.cvtColor(farm_img, cv2.COLOR_BGR2GRAY)

for scale in scales:
    resized_template=cv2.resize(cotton_img,None,fx=scale,fy=scale,interpolation=cv2.INTER_LINEAR)
    resized_template2=cv2.resize(potato_g_img,None,fx=scale,fy=scale,interpolation=cv2.INTER_LINEAR)


    result = cv2.matchTemplate(gray_img, resized_template, cv2.TM_CCOEFF_NORMED)
    result2 = cv2.matchTemplate(gray_img, resized_template2, cv2.TM_CCOEFF_NORMED)


    yloc, xloc = np.where(result >= threshold)
    yloc2, xloc2 = np.where(result2 >= threshold)



    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(resized_template.shape[1]), int(resized_template.shape[0])])


    for (x, y) in zip(xloc2, yloc2):
        rectangles2.append([int(x), int(y), int(resized_template2.shape[1]), int(resized_template2.shape[0])])



# min_val, max_value, min_loc, max_loc = cv2.minMaxLoc(result)
# len(rectangles1)


rectangles, weight = cv2.groupRectangles(rectangles, 1, 0.2)
rectangles2, weight2 = cv2.groupRectangles(rectangles2, 1, 0.2)


print(f"Number of rectangles: {len(rectangles)}")
print(f"Number of rectangles: {len(rectangles2)}")

for (x, y, w, h) in rectangles:
    # Draw the rectangle
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (255, 255, 255), 2)

    # Add the label "Cotton" near the rectangle
    label = "Cotton"
    font = cv2.FONT_HERSHEY_TRIPLEX
    font_scale = 0.6
    font_thickness = 1
    text_color = (255, 255, 255)  # Same color as the rectangle
    text_size = cv2.getTextSize(label, font, font_scale, font_thickness)[0]

    # Position the text above the rectangle
    text_x = x
    text_y = y - 10  # Slightly above the rectangle
    if text_y < 0:  # Ensure the text stays within bounds
        text_y = y + 20
    cv2.putText(farm_img, label, (text_x, text_y), font, font_scale, text_color, font_thickness)

for (x, y, w, h) in rectangles2:
    # Draw the rectangle
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (0, 255, 255), 2)

    # Add the label "Cotton" near the rectangle
    label2 = "Potato"
    font2 = cv2.FONT_HERSHEY_TRIPLEX
    font_scale2 = 0.6
    font_thickness2 = 1
    text_color2 = (0, 255, 255)  # Same color as the rectangle
    text_size2 = cv2.getTextSize(label2, font2, font_scale2, font_thickness2)[0]

    # Position the text above the rectangle
    text_x2 = x
    text_y2 = y - 10  # Slightly above the rectangle
    if text_y2 < 0:  # Ensure the text stays within bounds
        text_y2 = y + 20

    cv2.putText(farm_img, label2, (text_x2, text_y2), font2, font_scale2, text_color2, font_thickness2)



# Display the final image
cv2.imshow("Labeled Image", farm_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




