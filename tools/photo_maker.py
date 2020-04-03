import cv2

import os
from time import sleep

from tools.emotions_recognizer import EmotionsRecognizer


def make_frame(cap):
    """Function for making frames"""

    for i in range(30):
        cap.read()
    ret, frame = cap.read()
    return frame


class FrameAnalyzer:
    """Class for making photos and determining emotions"""
    def __init__(self, period, photo_storage_path, emotions):
        """
        FrameAnalyzer constructor

        :param period: period for making frames
        :param photo_storage_path: path to storage with photos
        :param emotions: emotions for determining
        """

        self.period = period
        self.path = photo_storage_path
        self.rec = EmotionsRecognizer(emotions)

    def analyze_photos(self):
        """Method for analyzing emotions on photos"""
        photo_count = 0
        cap = cv2.VideoCapture(0)
        while True:
            frame = make_frame(cap)
            frame_path = os.path.join(self.path, f'photo_{photo_count}.png')
            cv2.imwrite(frame_path, frame)
            prediction = self.rec.predict(os.path.join(frame_path))
            os.remove(frame_path)
            photo_count += 1
            sleep(self.period)
        cap.release()
