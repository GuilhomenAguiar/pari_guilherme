#!/usr/bin/env python
import cv2


def nothing(x):
    pass

def main():
    # define a video capture object
    vid = cv2.VideoCapture(0)
    video = cv2.namedWindow('mask')
    cv2.createTrackbar('Bmin', 'mask', 0, 255, nothing)
    cv2.createTrackbar('Bmax', 'mask', 255, 255, nothing)
    cv2.createTrackbar('Gmin', 'mask', 0, 255, nothing)
    cv2.createTrackbar('Gmax', 'mask', 255, 255, nothing)
    cv2.createTrackbar('Rmin', 'mask', 0, 255, nothing)
    cv2.createTrackbar('Rmax', 'mask', 255, 255, nothing)

    while True:

        # Capture the video frame
        # by frame
        _, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('video color', frame)

        l_b = cv2.getTrackbarPos('Bmin', 'mask')
        h_b = cv2.getTrackbarPos('Bmax', 'mask')
        l_g = cv2.getTrackbarPos('Gmin', 'mask')
        h_g = cv2.getTrackbarPos('Gmax', 'mask')
        l_r = cv2.getTrackbarPos('Rmin', 'mask')
        h_r = cv2.getTrackbarPos('Rmax', 'mask')

        lower_color = (l_b, l_g, l_r)
        upper_color = (h_b, h_g, h_r)

        mask = cv2.inRange(frame, lower_color, upper_color)

        cv2.imshow('mask', mask)


        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()







if __name__ == '__main__':
    main()