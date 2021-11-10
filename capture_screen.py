"""
Capture the screen suing mss Module, return the np.array with current screen.
Class contains method:
- grab_screen which allows to grab current screen from the toppest opened program in computer - it's the real view which is visiable for people.

"""

import logging
from typing import List
import cv2
import numpy as np
from mss import mss


class CaptureScreen:
    def __init__(self) -> None:
        """
        Initialize object of class.
        :param: None
        :return: None
        """
        pass
 
    def grab_screen(self):
        """
        Capture the current screen.
        :param: None
        :return: np.array of the image 
        """
        with mss() as sct:
            try:
                mon = sct.monitors[0]
                img = sct.grab(mon)
                img = np.array(img)
                return img

            except Exception as e:
                logging.error("Monitor is not available, check Your computer.")
                return -1
        
    

    def get_chessboard_colors(cls):
        pass
    
    @staticmethod
    def find_chessboard(img):
        """
        Find chessboard by searching corners, the function has two implications, there are depend on the color border, 
        more information in the next lines of function. Return coordinates of top left corner saved like tuple(y, x), 
        size of the chessboard tuple((height_of_the_chessboard, width_of_the_chessboard) and size of the field on the chessboard 
        tuple((height_of_the_field, width_of_the_field)

        Raise ValueError if chessboard not found.

        :param img: the image of the screen
        :return: tuple(y, x), tuple((height_of_the_chessboard, width_of_the_chessboard), tuple((height_of_the_field, width_of_the_field)
        """

        print(img.shape)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 160, 200, cv2.THRESH_BINARY_INV)[1]

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

        is_found = False

        # if corners are found break the loop and pass the type_of_board to next code
        for border in borders:
            is_found, corners = cv2.findChessboardCorners(thresh, border, cv2.CALIB_CB_ADAPTIVE_THRESH+cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)
            if is_found:
                # logging process
                logging.info("Chessboard bas been found.")

                # saved the first element from the tuple
                type_of_border = border[0]
                break
        
        if is_found:
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

            return (int(top_left_y), int(top_left_x)), (int(chessboard_width), int(chessboard_height)), (int(field_height) ,int(field_width))
        else:
            logging.warning("Chessboard cannot be found.")
            raise ValueError("Chessboard not found.")           