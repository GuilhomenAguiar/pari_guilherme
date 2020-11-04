#!/usr/bin/env python
import cv2


def main():
    # define a video capture object
    vid = cv2.VideoCapture(0)
    colorwindow = cv2.namedWindow("Color Segmentation")

    while True:

        # Capture the video frame
        # by frame
        _, frame = vid.read()

        # Display the resulting frame
        cv2.imshow(colorwindow, frame)

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