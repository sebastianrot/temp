class WhisperModel:
    def __init__(self, path):
        self.path = path

    def load_model(self):
        return f'laduje model whisper z sciezki {self.path}'

