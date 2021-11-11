"""
opencv save images as [len(y), len(x)]
"""

import logging
import cv2
from Log import Log
from capture_screen import CaptureScreen
from chessboard import ChessBoard
from time import sleep
from exceptions import ScreenNotBeFound, ChessBoardNotFound

# start logging, now every exception will be save in the file
Log()

# holder to the screen, allow to caprtue the current screen which is displeyed
screen_holder = CaptureScreen()


# init chessboard
chessboard = ChessBoard()


def main():
    
    # grab currend screen
    
    while True:

        try:
            image_of_screen = screen_holder.grab_screen()
        except ScreenNotBeFound:
            # give 2 seconds to do some operations on computer to for example run website to play chessbar
            sleep(2)
            # skip next lines of the code
            continue


        # find chessboard
        chessboard.find(image_of_screen)

        # try to get chessboad parameters
        try: 
            coordinates_of_chessboard = chessboard.get_cb_coordianates
            size_of_the_chessboard = chessboard.get_cb_size
            size_of_the_field = chessboard.get_f_size
        except ChessBoardNotFound as msg:
            logging.error(msg)
            continue
            
        
        top_left_y, top_left_x = coordinates_of_chessboard
        chessboard_height, chessboard_width = size_of_the_chessboard

        # displat test img od the chessboard
        cv2.imshow('test', image_of_screen[top_left_y:top_left_y + chessboard_height,top_left_x:top_left_x + chessboard_width])
        if cv2.waitKey(0):
            cv2.destroyAllWindows()



if '__main__' == __name__:
    main()