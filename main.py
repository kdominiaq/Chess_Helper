import time

import cv2
import numpy as np
from mss import mss


def record(name):
    with mss() as sct:
        mon = sct.monitors[0]

        while True:              
            img = sct.grab(mon)
            cv2.imshow('test', np.array(img))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break

record("Video")