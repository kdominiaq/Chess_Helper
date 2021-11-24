import numpy as np
import cv2
import logging

from exceptions import ChessBoardNotFound

class ChessBoard:
    
    def __init__(self) -> None:
        # is chessboard found
        self._is_found = False

        # chessboard image
        self._chessboard_image = np.array([])

        # coordinates of left top cotrner of the board, tuple (y, x)
        self._chessboard_coordiantes = [0, 0]

        # size of the chessboard and field, [width, height] contains widht and height of the chessboard, tuple(width, height) contains widht and height of the 
        self._chessboard_size = [0, 0]
        self._field_size = [0, 0]
        self._field_x, self._field_y = 106, 106
        # color of the chessboard [bright, dark], save as [R, G, B]:
        self._field_colors = np.array([])

        # player starts, bright pieces are on the bottom on the chessboard      
        self._notation_to_xy_position = [{'notation': 'a1', 'position': (self._field_y * 7, self._field_x * 0)},
                                         {'notation': 'a2', 'position': (self._field_y * 6, self._field_x * 0)},
                                         {'notation': 'a3', 'position': (self._field_y * 5, self._field_x * 0)},
                                         {'notation': 'a4', 'position': (self._field_y * 4, self._field_x * 0)},
                                         {'notation': 'a5', 'position': (self._field_y * 3, self._field_x * 0)},
                                         {'notation': 'a6', 'position': (self._field_y * 2, self._field_x * 0)},
                                         {'notation': 'a7', 'position': (self._field_y * 1, self._field_x * 0)},
                                         {'notation': 'a8', 'position': (self._field_y * 0, self._field_x * 0)},

                                         {'notation': 'b1', 'position': (self._field_y * 7, self._field_x * 1)},
                                         {'notation': 'b2', 'position': (self._field_y * 6, self._field_x * 1)},
                                         {'notation': 'b3', 'position': (self._field_y * 5, self._field_x * 1)},
                                         {'notation': 'b4', 'position': (self._field_y * 4, self._field_x * 1)},
                                         {'notation': 'b5', 'position': (self._field_y * 3, self._field_x * 1)},
                                         {'notation': 'b6', 'position': (self._field_y * 2, self._field_x * 1)},
                                         {'notation': 'b7', 'position': (self._field_y * 1, self._field_x * 1)},
                                         {'notation': 'b8', 'position': (self._field_y * 0, self._field_x * 1)},

                                         {'notation': 'c1', 'position': (self._field_y * 7, self._field_x * 2)},
                                         {'notation': 'c2', 'position': (self._field_y * 6, self._field_x * 2)},
                                         {'notation': 'c3', 'position': (self._field_y * 5, self._field_x * 2)},
                                         {'notation': 'c4', 'position': (self._field_y * 4, self._field_x * 2)},
                                         {'notation': 'c5', 'position': (self._field_y * 3, self._field_x * 2)},
                                         {'notation': 'c6', 'position': (self._field_y * 2, self._field_x * 2)},
                                         {'notation': 'c7', 'position': (self._field_y * 1, self._field_x * 2)},
                                         {'notation': 'c8', 'position': (self._field_y * 0, self._field_x * 2)},

                                         {'notation': 'd1', 'position': (self._field_y * 7, self._field_x * 3)},
                                         {'notation': 'd2', 'position': (self._field_y * 6, self._field_x * 3)},
                                         {'notation': 'd3', 'position': (self._field_y * 5, self._field_x * 3)},
                                         {'notation': 'd4', 'position': (self._field_y * 4, self._field_x * 3)},
                                         {'notation': 'd5', 'position': (self._field_y * 3, self._field_x * 3)},
                                         {'notation': 'd6', 'position': (self._field_y * 2, self._field_x * 3)},
                                         {'notation': 'd7', 'position': (self._field_y * 1, self._field_x * 3)},
                                         {'notation': 'd8', 'position': (self._field_y * 0, self._field_x * 3)},

                                         {'notation': 'e1', 'position': (self._field_y * 7, self._field_x * 4)},
                                         {'notation': 'e2', 'position': (self._field_y * 6, self._field_x * 4)},
                                         {'notation': 'e3', 'position': (self._field_y * 5, self._field_x * 4)},
                                         {'notation': 'e4', 'position': (self._field_y * 4, self._field_x * 4)},
                                         {'notation': 'e5', 'position': (self._field_y * 3, self._field_x * 4)},
                                         {'notation': 'e6', 'position': (self._field_y * 2, self._field_x * 4)},
                                         {'notation': 'e7', 'position': (self._field_y * 1, self._field_x * 4)},
                                         {'notation': 'e8', 'position': (self._field_y * 0, self._field_x * 4)},

                                         {'notation': 'f1', 'position': (self._field_y * 8, self._field_x * 5)},
                                         {'notation': 'f2', 'position': (self._field_y * 6, self._field_x * 5)},
                                         {'notation': 'f3', 'position': (self._field_y * 5, self._field_x * 5)},
                                         {'notation': 'f4', 'position': (self._field_y * 4, self._field_x * 5)},
                                         {'notation': 'f5', 'position': (self._field_y * 3, self._field_x * 5)},
                                         {'notation': 'f6', 'position': (self._field_y * 2, self._field_x * 5)},
                                         {'notation': 'f7', 'position': (self._field_y * 1, self._field_x * 5)},
                                         {'notation': 'f8', 'position': (self._field_y * 0, self._field_x * 5)},

                                         {'notation': 'g1', 'position': (self._field_y * 7, self._field_x * 6)},
                                         {'notation': 'g2', 'position': (self._field_y * 6, self._field_x * 6)},
                                         {'notation': 'g3', 'position': (self._field_y * 5, self._field_x * 6)},
                                         {'notation': 'g4', 'position': (self._field_y * 4, self._field_x * 6)},
                                         {'notation': 'g5', 'position': (self._field_y * 3, self._field_x * 6)},
                                         {'notation': 'g6', 'position': (self._field_y * 2, self._field_x * 6)},
                                         {'notation': 'g7', 'position': (self._field_y * 1, self._field_x * 6)},
                                         {'notation': 'g8', 'position': (self._field_y * 0, self._field_x * 6)},

                                         {'notation': 'h1', 'position': (self._field_y * 7, self._field_x * 7)},
                                         {'notation': 'h2', 'position': (self._field_y * 6, self._field_x * 7)},
                                         {'notation': 'h3', 'position': (self._field_y * 5, self._field_x * 7)},
                                         {'notation': 'h4', 'position': (self._field_y * 4, self._field_x * 7)},
                                         {'notation': 'h5', 'position': (self._field_y * 3, self._field_x * 7)},
                                         {'notation': 'h6', 'position': (self._field_y * 2, self._field_x * 7)},
                                         {'notation': 'h7', 'position': (self._field_y * 1, self._field_x * 7)},
                                         {'notation': 'h8', 'position': (self._field_y * 0, self._field_x * 7)}]

    @property
    def get_cb_coordianates(self):
        """
        Shortcut "cb" means chessboard.

        :return chessboard_coordiantes: list(y, x) of the left top corner
        """
        if self._is_found:
            return self._chessboard_coordiantes
        else:
            raise ChessBoardNotFound("chessboard_coordiantes")
        

    @property
    def get_cb_size(self):
        """
        Shortcut "cb" means chessboard.

        :return chessboard_size: list(width, height) of the chessboard.
        """
        if self._is_found:
            return self._chessboard_size
        else:
            raise ChessBoardNotFound("chessboard_size")

    
    @property
    def get_f_size(self):
        """
        Shortcut "f" mens field.

        :return field_size: list(width, height) of the field.
        """
        if self._is_found:
            return self._field_size
        else:
            raise ChessBoardNotFound("field_size")


    @property
    def get_f_colors(self):
        """
        Shortcut "f" means field.

        :return field_colors: list(bright, dark) of the field, colors have been saved as list[R, G, B]
        """
        if self._is_found:
            return self._field_colors
        else:
            raise ChessBoardNotFound("field_colors")


    @property
    def get_cb_image(self):
        """
        Shortcut "cb" means fchessboard.

        :return chessboard_image: raedy to disply by cv2.imshow
        """
        if self._is_found:
            return self._chessboard_image
        else:
            raise ChessBoardNotFound("field_colors")


    def _find_chessboard_colors(self):
        """
        Find color of the bright and ark field on the board by check right top corner of the field which is on left top croner on the chess board and top right corner.
        Colors will be found by these two fields (checked by B - Bright, D - Dark):
        B . . . . . . D
        . . . . . . . .
        | | | | | | | |
        . . . . . . . . 

        Now in field "X" color will be found by area which is picked by "x":
        . . . . . . . .
        . . . . . . x .  
        . . . . . . . . 
        . . . . . . . .
        | | | | | | | |
        . . . . . . . .

        :return colors: list(bright_color, dark_color) of the fields, colors have been saved as list[R, G, B]
        """

        _, dx_cb = self._chessboard_size
        dy_f, dx_f = self._field_size

        # It will not be changed
        y_target = int(round(dy_f /8))
    
        # Bright color
        x_target = int(dx_f - round(dx_f /8))
        bright_color = self._chessboard_image[y_target,x_target]

        # Dark color
        x_target = int(dx_cb - round(dx_f / 8))
        dark_color = self._chessboard_image[y_target,x_target]

        # Assign varaibles to class' varaibles and cut the last value from the list (because it's depth)
        bright_color = bright_color[:-1]
        dark_color = dark_color[:-1]

        return [bright_color, dark_color]


    def find(self, img) -> None:
        """
        Find chessboard by searching corners, the function has two implications, there are depend on the color border, 
        more information in the next lines of function. Assign True to  if is found, otherwise False.

        :param img: the image of the screen
        :return: None
        """
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 180, 184, cv2.THRESH_BINARY_INV)[1]
        
        # There are two possibilities of chessboards, one of them can be surrounded by the dark color, the second one can be surrounded by bright color.
        # Because the code uses the inverse of binary threshes is necessary to create two situations:
        # - the first one is when the chessboard is surrounded by the dark color, we can easily spot 49 (7 x 7) points on the board which are on the corners of fields
        # - the second one is when the chessboard is surrounded by a bright color, this time we can spot only 25 (5 x 5) points, because the border fields aren't recognized
        # so we can only look for correct filedd in the center of the board.
        bright_border = (5, 5)
        dark_border = (7, 7)

        borders = np.array([dark_border, bright_border])

        # saving information about found chessboard, which border is present :
        # - 5 -> bright_border
        # - 7 -> dark_border
        type_of_border = None

        self._is_found = False

        # if corners are found break the loop and pass the type_of_board to next code
        for border in borders:
            self._is_found, corners = cv2.findChessboardCorners(thresh, border, cv2.CALIB_CB_ADAPTIVE_THRESH+cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)
            if self._is_found:
                # logging process
                logging.info("Chessboard bas been found.")

                # saved the first element from the tuple
                type_of_border = border[0]
                break
        
        if self._is_found:
            # looking for top left corner(tp) of the 
            field_height, field_width = 0, 0
            
            # coordinates of the top left corner are saved in the first element form corners list, next corner is saved in next index
            top_left_x, top_left_y = corners[0][0]
            next_to_top_left_corner_x,_ = corners[1][0]

            # the second element from the corners list contains (x, y), but this time x value is increased by width field, 
            # so the width of the field will be, result from subtracting the second corner with the first corner (only for x values)
            # width and height are equal because the field is the square        
            field_width = next_to_top_left_corner_x - top_left_x
            field_height = field_width
            
            # cutting image to display only chessboard, the top left corner can be in two places (beetwen % mark):
            # - dark_border:        - bright_border
            #   X X . . . . . .       . . . . . . . .
            #   X X . . . . . .       . X X . . . . .
            #   . . . . . . . .       . X X . . . . . 
            #   . . . . . . . .       . . . . . . . .
            #   . . . . . . . .       . . . . . . . .
            #   . . . . . . . .       . . . . . . . .    
            #   . . . . . . . .       . . . . . . . .
            #   . . . . . . . .       . . . . . . . . 

            # saving information about found chessboard, which border is present :
            # - 5 -> bright_border
            # - 7 -> dark_border
            if type_of_border == 5:
                top_left_x -= 2 * field_width
                top_left_y -= 2 * field_height
            elif type_of_border == 7:
                top_left_x -= field_width
                top_left_y -= field_height
            
            chessboard_width, chessboard_height = field_width * 8, field_height * 8       
            
            # assign class varaivbles
            self._chessboard_coordiantes = np.array([int(top_left_y), int(top_left_x)])
            self._chessboard_size = np.array([int(chessboard_width), int(chessboard_height)])
            self._field_size = np.array([int(field_width), int(field_height)])
            self._chessboard_image = img[int(top_left_y):int(top_left_y + chessboard_height),int(top_left_x):int(top_left_x + chessboard_width)]

            self._field_colors = self._find_chessboard_colors()


        else:
            logging.warning("Chessboard cannot be found.")


    def _get_xy_from_chess_notation(self, notation):
        """
        Returns position of 'X' and 'Y' by chess notation. Function scan list '_notation_to_xy_position'
        for dict with the same notation like passing notation. Example: passing 'a1' -> return (0,700), example is true
        if height and width of chess board i 800x800.
        :param notation: chess notation to one field, like 'a1'
        :return: tuple with x and y value
        """
        for i in self._notation_to_xy_position:
            key = i.get('notation')
            if key == notation:
                return i.get('position')

    def _get_chess_notation_from_xy(self, yx):
        """
        Returns chess notation by 'X' and 'Y' coordiantes of the field. Function scan list '_notation_to_xy_position'
        for dict with the same notation like passing notation. Example: passing 'a1' -> return (0,700), example is true
        if height and width of chess board i 800x800.
        :param xy: chess notation to one field, like [y,x]
        :return: string with notation
        """
        print(yx)
        for i in self._notation_to_xy_position:
            key = i.get('position')
            if key == yx:
                return i.get('notation')