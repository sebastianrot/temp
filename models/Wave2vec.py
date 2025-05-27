class Wave2vecModel:
    def __init__(self, path):
        self.path = path

    def load_model(self):
        return f'laduje model wave2vec z sciezki {self.path}'