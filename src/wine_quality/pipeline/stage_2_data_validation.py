from wine_quality.config.configuration import ConfigurationManager
from wine_quality.components.data_validation import DataValidation
from wine_quality import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            #data_validation.validate_all_files_exist()
            data_validation.validate_all_columns()
        except Exception as e:
            raise e