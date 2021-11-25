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
from exceptions import ScreenNotBeFound, ChessBoardNotFound, IndexOutOfChessBoard

# start logging, now every exception will be save in the file
Log()

# holder to the screen, allow to caprtue the current screen which is displeyed
screen_holder = CaptureScreen()

# init chessboard
chessboard = ChessBoard()

# init game logic
logic = LogicGame()
def main():
    is_screen_found = False
    is_chessboard_found = False
    rdy_to_play = False
    # grab currend screen
    

    while True:
            if not is_chessboard_found and (is_screen_found or not is_screen_found):
                try:
                    image_of_screen = screen_holder.grab_screen()
                    is_screen_found = True
                except ScreenNotBeFound:
                    # give 2 seconds to do some operations on computer to for example run website to play chess
                    sleep(2)

                    # skip next lines of the code
                    continue

                try: 
                    # find chessboard
                    chessboard.find(image_of_screen)
                    is_chessboard_found = True

                    # try to get chessboad parameters
                    coordinates_of_chessboard = chessboard.get_cb_coordianates
                    size_of_the_chessboard = chessboard.get_cb_size
                    size_of_the_field = chessboard.get_f_size
                    chessboard_image = chessboard.get_cb_image
                except ChessBoardNotFound as msg:
                    logging.error(msg)
                    sleep(2)
                    continue
                except IndexOutOfChessBoard:
                    sleep(2)
                    continue
            
            elif is_chessboard_found and is_screen_found:
                # crap display screen
                image_of_screen = screen_holder.grab_screen()
                
                # update chessboardview
                chessboard.update_view(image_of_screen)

                # inicializate logic of game
                if not rdy_to_play: 
                    logic.set_chessboard(chessboard)
                    rdy_to_play = logic.is_chessboard_ready_to_start()

                    # waitnig one second fo restart the game (chess) by user
                    sleep(1)
                    
                if rdy_to_play:
                    logic.start_game()
    
                # clear memory
                del image_of_screen
                sleep(0.1)
       


if '__main__' == __name__:
    main()