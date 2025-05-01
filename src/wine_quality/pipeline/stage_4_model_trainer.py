from wine_quality.config.configuration import ConfigurationManager
from wine_quality.components.model_trainer import ModelTrainer
from wine_quality import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e
