"""
This Python script shows why we need to convert the image to grayscale 
and why other single channel values like R, G, and B, do not work well for
contour detection.
"""
import os
import time
import cv2
import logging

def main():
    # read the image
    image = cv2.imread('image_2.jpg')
    directory = "channel_experiment_output"
    parent_dir = "/data/"
    path = os.path.join(parent_dir, directory)
    if os.path.exists(path):
        print("{} folder exists".format(directory))
    else:
        os.mkdir(path)
    # B, G, R channel splitting
    blue, green, red = cv2.split(image)

    # detect contours using blue channel and without thresholding
    contours1, hierarchy1 = cv2.findContours(image=blue, mode=cv2.RETR_TREE, 
                                             method=cv2.CHAIN_APPROX_NONE)

    # draw contours on the original image
    image_contour_blue = image.copy()
    cv2.drawContours(image=image_contour_blue, contours=contours1, contourIdx=-1, 
                     color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    # see the results
    logging.info("Generating blue channel image")
    cv2.imwrite(os.path.join(path, 'blue_channel.jpg'), image_contour_blue)

    # detect contours using green channel and without thresholding
    contours2, hierarchy2 = cv2.findContours(image=green, mode=cv2.RETR_TREE, 
                                             method=cv2.CHAIN_APPROX_NONE)
    # draw contours on the original image
    image_contour_green = image.copy()
    cv2.drawContours(image=image_contour_green, contours=contours2, contourIdx=-1, 
                     color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    # see the results
    logging.info("Generating green channel image")
    cv2.imwrite(os.path.join(path, 'green_channel.jpg'), image_contour_green)

    # detect contours using red channel and without thresholding
    contours3, hierarchy3 = cv2.findContours(image=red, mode=cv2.RETR_TREE, 
                                           method=cv2.CHAIN_APPROX_NONE)
    # draw contours on the original image
    image_contour_red = image.copy()
    cv2.drawContours(image=image_contour_red, contours=contours3, contourIdx=-1, 
                     color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    # see the results
    logging.info("Generating red channel image")
    cv2.imwrite(os.path.join(path, 'red_channel.jpg'), image_contour_red)
    print("sleeping for some time")
    time.sleep(60)

if __name__ == '__main__':
    main()
