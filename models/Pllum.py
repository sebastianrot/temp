class PllumModel:
    def __init__(self, path):
        self.path = path

    def load_model(self):
        return f'laduje model pllum z sciezki {self.path}'