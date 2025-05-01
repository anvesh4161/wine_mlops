import pandas as ps
import os
from wine_quality import logger
from sklearn.linear_model import ElasticNet
import joblib
from wine_quality.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info(f"Training model {self.config.model_name}")

        train_data = ps.read_csv(self.config.train_data_path)
        test_data = ps.read_csv(self.config.test_data_path)

        logger.info(f"Train data shape: {train_data.shape}")
        logger.info(f"Test data shape: {test_data.shape}")

        X_train = train_data.drop(columns=[self.config.target_column], axis=1)
        y_train = train_data[self.config.target_column]
        X_test = test_data.drop(columns=[self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(X_train, y_train)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))

        
