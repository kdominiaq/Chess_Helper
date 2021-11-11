"""
Capture the screen suing mss Module, return the np.array with current screen.
Class contains method:
- grab_screen which allows to grab current screen from the toppest opened program in computer - it's the real view which is visiable for people.

"""

from exceptions import ScreenNotBeFound
import logging
from typing import List
import cv2
import numpy as np
from mss import mss


class CaptureScreen:
    def __init__(self) -> None:
        """
        Initialize object of class. Variable "send_log" provides send only one log - resposible only for logging.info("Image of the screen is found.").
        :param: None
        :return: None
        """
        self._send_log = True
 
    def grab_screen(self):
        """
        Capture the current screen. Raise ScreenNotBeFound excpetion when something goes wrong.
        :param: None
        :return: np.array of the image 
        """
        with mss() as sct:
            try:
                mon = sct.monitors[0]
                img = sct.grab(mon)
                img = np.array(img)
                if self._send_log:
                    logging.info("Image of the screen is found.")
                    # log has been sent
                    self._send_log = False
                return img

            except IndexError as e:
                logging.error("Monitor is not available, check Your computer.")
                # monitor is not available, than log about is_found can be send another time.
                self._send_log = True
                raise ScreenNotBeFound