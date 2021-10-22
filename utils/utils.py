import numpy as np
import cv2
import base64

class Utils:
    @staticmethod
    def imageToBase64(image):
        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer)
        return jpg_as_text
