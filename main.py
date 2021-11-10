"""
opencv save images as [len(y), len(x)]
"""

import logging
import cv2
from Log import Log
from capture_screen import CaptureScreen

# start logging, now every exception will be save in the file
Log()

# holder to the screen, allow to caprtue the current screen which is displeyed
screen_holder = CaptureScreen()

def main():
    
    # grab currend screen
    
    while True:
        try:
            image_of_screen = screen_holder.grab_screen()

            # get information about chessboard
            coordinates_of_chessboard, size_of_the_chessboard , size_of_the_field = screen_holder.find_chessboard(image_of_screen)
            top_left_y, top_left_x = coordinates_of_chessboard
            chessboard_height, chessboard_width = size_of_the_chessboard

            # displat test img od the chessboard
            cv2.imshow('test', image_of_screen[top_left_y:top_left_y + chessboard_height,top_left_x:top_left_x + chessboard_width])
            if cv2.waitKey(0):
                cv2.destroyAllWindows()
        # Exception throw by find_chessboad()
        except ValueError:
            print('Can not find chessboard, please run the game on computer and make it displayed')


if '__main__' == __name__:
    main()