import os
from tools.emotions_recognizer import EmotionsRecognizer


def test_recognizer():
    rec = EmotionsRecognizer()
    test_path = os.path.join(os.getcwd(), "files_for_tests")
    predictions = []
    right_emotions = ['happiness', 'surprise', 'disgust']
    for file in os.listdir(test_path):
        predictions.append(rec.predict(os.path.join(test_path, file)))

    assert predictions == right_emotions

