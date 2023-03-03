import cv2
import numpy as np

# range of red manually defined
img = cv2.imread('stop_sign_ok.jpeg')
hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low_red = np.array([76, 53, 228])
high_red = np.array([114, 92, 255])

red_mask = cv2.inRange(hsv_frame, low_red, high_red)
red = cv2.bitwise_and(img, img, mask=red_mask)
