# capture single image from webcam using python

# importing OpenCV library
# pip3 install opencv-python
import cv2 as cv
import time

# initialize the camera
cam_port = 0
cam = cv.VideoCapture(cam_port)

# wait for 2 seconds to adjust the camera lights, else picture will be always dark
time.sleep(2)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error, show result
if result:

    # showing result, it take frame name and image output
    cv.imshow("My Cam Pic", image)

    # saving image in local storage
    cv.imwrite("cam_capture.jpg", image)

    # If keyboard interrupt occurs, destroy image window
    cv.waitKey(0)
    cv.destroyWindow("My Cam Pic")

# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")
