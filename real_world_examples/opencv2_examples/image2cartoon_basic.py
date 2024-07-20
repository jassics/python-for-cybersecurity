# importing libraries
# pip install opencv-python
import cv2
import numpy as np

# reading image
img = cv2.imread("jassi.jpg")

# Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                         cv2.THRESH_BINARY, 9, 5)

# Cartoonization
color = cv2.bilateralFilter(img, 9, 200, 200)
cartoon = cv2.bitwise_and(color, color, mask=edges)

#cv2.imshow("Image", img)
#cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)


color = cv2.bilateralFilter(img, d=9, sigmaColor=200,sigmaSpace=200)
cv2.imshow("Color", color)

def color_quantization(img, k):
# Defining input data for clustering
  data = np.float32(img).reshape((-1, 3))
# Defining criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
# Applying cv2.kmeans function
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result

img_1 = color_quantization(img, 9)
cv2.imshow("Quant", img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
