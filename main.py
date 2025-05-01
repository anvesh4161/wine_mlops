from wine_quality import logger
from wine_quality.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from wine_quality.pipeline.stage_2_data_validation import DataValidationPipeline
from wine_quality.pipeline.stage_3_data_transformation import DataTransformation
from wine_quality.pipeline.stage_4_model_trainer import ModelTrainerPipeline
from wine_quality. config.configuration import ConfigurationManager


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    config_manager = ConfigurationManager()
    data_transformation_config = config_manager.get_data_transformation_config()
    
    # Pass the configuration to DataTransformation
    data_transformation = DataTransformation(config=data_transformation_config)
    data_transformation.train_test_splitting()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e