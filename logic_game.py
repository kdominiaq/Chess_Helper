from numpy.lib.utils import lookfor
from chessboard import ChessBoard
import logging
import numpy as np

class LogicGame(ChessBoard):
    def __init__(self, chessboard: ChessBoard) -> None:
        # assign chessboard to private varaible to get infomration about board
        self._cb = chessboard
        
        # white - 0, black - 1
        self._opponent_color = 0
        self._player_color = 0
        



    def which_color_have_players(self):
        """
        Working on the given chessboard image, check the color of the rocks on the left side of the board - compare to each other, 
        if the sum of RGB representation of color is smaller then second, it's black (because it is darker than it.)        
        If the color of the rock is black, it means the player has white color, and "we" start the game. Otherwise, the opponent starts 
        the game (has white in color).
        
        Assign colors to variables (_opponent_color and _player_color).
        """       
        # Looking fot the center of the field where towers are.
        # T - tower on  the top of board, B - on the bot.
        #   T . . . . . . .       
        #   . . . . . . . .       
        #   . . . . . . . .       
        #   . . . . . . . .       
        #   . . . . . . . .       
        #   . . . . . . . .        
        #   . . . . . . . .      
        #   B . . . . . . .       

        # counte center of the fileds
        tower_T_coordinates_y = int(self._cb.get_f_size[0] / 2)
        tower_T_coordinates_x = int(self._cb.get_f_size[1] / 2)

        tower_B_coordinates_y = self._cb.get_cb_size[0]  - int(self._cb.get_f_size[0] / 2)
        tower_B_coordinates_x = int(self._cb.get_f_size[1] / 2)

        # save color color of the fields
        tower_T_color = self._cb.get_cb_image[tower_T_coordinates_y,tower_T_coordinates_x]

        tower_B_color = self._cb.get_cb_image[tower_B_coordinates_y,tower_B_coordinates_x]
        
        # first three arguments of the list contains RGB, so nao assume the values
        tower_T_color = np.sum(tower_T_color[::-1])
        
        tower_B_color = np.sum(tower_B_color[::-1])
        
        # compare values, gretter value means in this field is darker piece then second.
        # white pieces - 0
        # black pieces - 1
        if tower_T_color > tower_B_color:
            # assign colot to class values
            self._player_color = 1
            self._opponent_color = 0 
            
            # send log to file
            logging.info("Player color: Black, Opponent color: White.")
        else:
            self._player_color = 0
            self._opponent_color = 1
            
            logging.info("Player color: White, Opponent color: Black.")

    