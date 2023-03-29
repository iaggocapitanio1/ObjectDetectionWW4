import cv2 as cv
import numpy
from utils.functions import get_ratio_pixels_millimeters, draw_corners, draw_enumerate, get_bounding_box, transform

path = "./img/1.jpg"
frame = cv.imread(path)

original: numpy.ndarray = frame
cv.imwrite('original.jpg', frame)
threshold_minVal = 100
threshold_maxVal = 250
gaussian_kernel_size = (9, 9)
dilatation = numpy.ones((3, 3))
min_area_filter = 2000  # square pixels


while True:
    original = frame
    cv.imshow('frame', frame)
    ratio = get_ratio_pixels_millimeters(img=frame)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.GaussianBlur(frame, ksize=gaussian_kernel_size, sigmaX=1)
    frame = cv.Canny(image=frame, threshold1=threshold_minVal, threshold2=threshold_maxVal)
    frame = cv.dilate(frame, kernel=dilatation, iterations=2)
    frame = cv.erode(frame, kernel=dilatation, iterations=2)
    contours, hierarchy = cv.findContours(frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv.contourArea(contour)
        if area > min_area_filter:
            clean_contour_points = cv.approxPolyDP(contour, epsilon=0.01 * cv.arcLength(contour, True), closed=True)
            frame = cv.polylines(original, pts=clean_contour_points, isClosed=True, color=(255, 0, 0), thickness=12,
                                 lineType=cv.LINE_AA)
            bounding_box = get_bounding_box(img=frame, corners=clean_contour_points, draw=True)
            draw_corners(img=frame, corners=clean_contour_points, ratio=ratio, color=(0, 255, 155))
            draw_enumerate(img=frame, corners=clean_contour_points)
            cv.imshow("Frame", frame)
            cv.imwrite('output.jpg', frame)
            print(f"Normalized corners are: \n {transform(clean_contour_points, *bounding_box)}")

    key = cv.waitKey(0)
    if key:
        break
cv.destroyAllWindows()
