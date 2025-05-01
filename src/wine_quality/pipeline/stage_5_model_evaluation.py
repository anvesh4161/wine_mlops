from wine_quality.config.configuration import ConfigurationManager
from wine_quality.components.model_evaluation import ModelEvaluation
from wine_quality import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.save_results()
        except Exception as e:
            raise e
