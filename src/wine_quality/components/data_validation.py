import os
from wine_quality import logger
import pandas as pd
from wine_quality.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validate all columns in the dataset against the schema
        """
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = self.config.all_schema.keys()

            all_schema = self.config.all_schema.keys()

            for column in all_columns:
                if column not in all_schema:
                    validation_status = False
                    logger.info(f"Column {column} is not in the schema")
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Column {column} is not in the schema\n")

                else:
                    validation_status = True
                    logger.info(f"Column {column} is in the schema")
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Column {column} is in the schema\n")

            return validation_status

        except Exception as e:
            raise e



