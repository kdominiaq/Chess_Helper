"""
opencv save images as [len(y), len(x)]
"""

import logging
import cv2
from logic_game import LogicGame
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
            # give 2 seconds to do some operations on computer to for example run website to play chess
            sleep(2)
            # skip next lines of the code
            continue
        try: 
            # find chessboard
            chessboard.find(image_of_screen)

            # try to get chessboad parameters
            coordinates_of_chessboard = chessboard.get_cb_coordianates
            size_of_the_chessboard = chessboard.get_cb_size
            size_of_the_field = chessboard.get_f_size
            chessboard_image = chessboard.get_cb_image
            a = LogicGame(chessboard)
            a.which_color_have_players()
            print(a.is_chessboard_ready_to_start())
        except ChessBoardNotFound as msg:
            logging.error(msg)
            sleep(2)
            continue

        # displat test img od the chessboard
        cv2.imshow('test', chessboard_image)
        if cv2.waitKey(0):
            cv2.destroyAllWindows()


if '__main__' == __name__:
    main()