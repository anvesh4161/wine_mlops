from wine_quality.config.configuration import ConfigurationManager
from wine_quality.components.data_transformation import DataTransformation
from wine_quality import logger

STAGE_NAME = "Data Transformation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            #with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
             #   status = f.read().split(" ")[-1]

            #if status == True:
            logger.info("Data Validation is successful")
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_splitting()

            #else:
             #   raise Exception("Data Validation is not successful. Data Schema is not valid.")

        except Exception as e:
            raise e