"""
Class creates logging holder and file to contain all logs.
        
"""

import logging 
import os
import pathlib

from time import gmtime, strftime, sleep

class Log:
    def __init__(self) -> None:
        print("log init")
        self._logs_folder()
        logging.basicConfig(filename='logs/{}.log'.format(self._get_current_time()), 
                            format='%(levelname)s: %(asctime)s: %(message)s', 
                            level=logging.INFO)

        self.__start()

    @staticmethod
    def __start():
        """
        Create first message to user and start logging process.
        :param: None.
        :return: None.
        """
        try:
            username = os.getlogin()
            message = "Log started, enjoy the game {}!".format(username)
            logging.info(message)
        except Exception as e:
            print(e)
            return -1


    @staticmethod
    def _logs_folder():
        """
        Create a logs directory if it doesn't exist.
        :param: None.
        :return: None.
        """

        # get absolute path to project
        try:
            absolute_path = pathlib.Path().resolve()
            direciory_name = "logs"

            # create final the path with directory name
            path = os.path.join(absolute_path, direciory_name)
            is_exist = os.path.exists(path)
            # if the directory does not exist create it
            if not is_exist:
                os.makedirs(path)
                
        except Exception as e:
            print(e)

            return -1


    def _get_current_time(self):
        """
        Return current time, sytnax is:
        Year-Month-Day (Hour:Minute:Second)
        2000-01-01 (10:12:45)

        :param: none
        :return: current time
        """

        try: 
          current_time = strftime("%Y-%m-%d (%H:%M:%S)", gmtime())
        except Exception as e:
            print(e)
            return -1

        return current_time

