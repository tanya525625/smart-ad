from tools.photo_maker import FrameAnalyzer

if __name__ == "__main__":
    path_to_photos = "photos"
    period = 10
    emotions = ['happiness', 'disgust', 'surprise']

    ph_maker = FrameAnalyzer(period, path_to_photos, emotions)
    ph_maker.analyze_photos()


