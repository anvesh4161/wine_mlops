import os
from wine_quality import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from wine_quality.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

        # You can add different transformation techniques like scaling, encoding, etc. here
        # We can also perfomr different kinds of EDA before passing it to ML model
        # For now, we will just split the data into train and test sets, as the data is already clean

    def train_test_splitting(self):
        """Splitting the data into train and test sets"""
        logger.info("Splitting the data into train and test sets")

        # Read the data
        data = pd.read_csv(self.config.data_path)

        # Split the data into train and test sets
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        # Save the train and test sets to the root directory
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data split into train and test sets")
        logger.info(f"Train set saved to {os.path.join(self.config.root_dir, 'train.csv')}")
        logger.info(f"Test set saved to {os.path.join(self.config.root_dir, 'test.csv')}")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
