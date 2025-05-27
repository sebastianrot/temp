import config
from models import WhisperModel, Wave2vecModel, BielikAIModel, PllumModel

class FactorySTT:
    @staticmethod
    def create_stt_model(model, path):
        if model == "Whisper":
            whisper = WhisperModel(path)
            return whisper
        elif model == "Wave2vec":
            wave2vec = Wave2vecModel(path)
            return wave2vec
        else:
            raise ValueError(f"Nieznany model STT: {model}")


class FactoryLLM:
    @staticmethod
    def create_llm_model(model, path):
        if model == "BielikAI":
            bielik = BielikAIModel(path)
            return bielik
        elif model == "Pllum":
            pllum = PllumModel(path)
            return pllum
        else:
            raise ValueError(f"Nieznany model STT: {model}")

def main():
    test = FactorySTT.create_stt_model(config.STT_MODEL, config.DESCS_TEMPLATES_PATH)
    test2 = FactoryLLM.create_llm_model(config.TTT_MODEL, config.DESCS_TEMPLATES_PATH)
    print(test.load_model())
    print(test2.load_model())

if __name__ == "__main__":
    main()