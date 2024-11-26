import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

image_path = '7.jpg'
img = cv2.imread(image_path)

reader = easyocr.Reader(['en'], gpu=False)
imgtext = reader.readtext(img)
threshold = 0.25

for t_, t in enumerate(imgtext):
    box, text, score = t
    if score > threshold:
        box = [(int(point[0]), int(point[1])) for point in box]
        print(box, text, score)
        top_left = box[0]
        bottom_right = box[2]
        cv2.rectangle(img, box[0], box[2], (0, 255, 0), 2)
        cv2.putText(img, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off') 
plt.show()
