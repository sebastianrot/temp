class BielikAIModel:
    def __init__(self, path):
        self.path = path

    def load_model(self):
        return f'laduje model bielik z sciezki {self.path}'