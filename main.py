import os
from tools.emotions_recognizer import EmotionsRecognizer


if __name__ == "__main__":
    path_to_photos = "photos"
    emotions = ['happiness', 'anger']
    rec = EmotionsRecognizer(emotions)
    for photo in os.listdir(path_to_photos):
        prediction = rec.predict(os.path.join(path_to_photos, photo))