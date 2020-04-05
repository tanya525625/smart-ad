from cv2 import cv2
import sqlalchemy
import logging

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
        conn = connect_to_db()
        photo_count = 0
        cap = cv2.VideoCapture(0)
        while True:
            frame = make_frame(cap)
            frame_path = os.path.join(self.path, f'photo_{photo_count}.png')
            cv2.imwrite(frame_path, frame)
            prediction = self.rec.predict(os.path.join(frame_path))
            save_pred_to_db(conn, prediction)
            os.remove(frame_path)
            photo_count += 1
            sleep(self.period)
        cap.release()

def connect_to_db():
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASS")
    db_name = os.environ.get("DB_NAME")
    cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

    db = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_pass,
            database=db_name,
            query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)}
        )
    )
    conn = db.connect()

    return conn

def save_pred_to_db(conn, prediction):
    board_id = os.environ.get("BOARD_ID")
    emot_id = conn.execute(
        "SELECT emot_id FROM emotions WHERE emot_name=\""+prediction+"\";"
    ).fetchall()[0][0]
    conn.execute("INSERT INTO records(emot_id, board_id) "
                 "VALUES("+str(emot_id)+", "+str(board_id)+");")
