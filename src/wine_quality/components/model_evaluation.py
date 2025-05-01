import os
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from urllib.parse import urlparse
import numpy as np
import joblib
from wine_quality.config.configuration import ConfigurationManager
from pathlib import Path
from wine_quality.utils.common import save_json
from wine_quality.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        r2 = r2_score(actual, pred)
        mae = mean_absolute_error(actual, pred)
        mse = mean_squared_error(actual, pred)
        rmse = np.sqrt(mse)

        return r2, mae, mse, rmse
    
    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop(columns=[self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]

        predicted_values = model.predict(X_test)

        (r2, mae, mse, rmse) = self.eval_metrics(y_test, predicted_values)

        #Saving the metrices in a json file

        metrics = {"rmse": rmse, "r2": r2, "mae": mae, "mse": mse}
        save_json(path = Path(self.config.metric_file_name), data = metrics)