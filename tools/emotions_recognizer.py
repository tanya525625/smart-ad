from edEmoPy.src.fermodel import FERModel


class EmotionsRecognizer:
    """Class for emotions' recognition"""
    def __init__(self, emotions: list = ['happiness', 'disgust', 'surprise']):
        """
        EmotionsRecognizer constructor

        :param emotions: list of emotions for recognition,
        possible values: ['anger', 'fear', 'calm', 'sadness',
                          'happiness', 'surprise', 'disgust']
        """
        self.emotions = emotions
        self.model = FERModel(emotions, verbose=True)

    def predict(self, img_path: "str"):
        """
        Method for making prediction of the person's emotions in the photo

        :param img_path: path to the image for emotions recognition
        :return: emotion
        """

        return self.model.predict(img_path)

