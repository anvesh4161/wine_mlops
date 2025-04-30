import os
import urllib.request as request
import zipfile
from pathlib import Path
from typing import List
from wine_quality import logger
from wine_quality.utils.common import get_size
from wine_quality.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename} of size: {get_size(filename)}")

        else:
            logger.info(f"File already exists: {self.config.local_data_file} of size: {get_size(self.config.local_data_file)}")

    def extract_zip_file(self):
        """Extracts the zip file.
        zip_file_path: str
        Function to extract the zip file.
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)