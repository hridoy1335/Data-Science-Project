import os
import sys
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.exception import CustomException
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestion:
    TRAIN_DATA_PATH:str = os.path.join('artifacts','train.csv')
    TEST_DATA_PATH:str = os.path.join('artifacts','test.csv')
    RAW_DATA_PATH:str = os.path.join('artifacts','raw.csv')
    
class DataIngestionConfig:
    def __init__(self):
        self.ingestionconfig = DataIngestion()
        
    def get_data_ingestion_path(self):
        try:
            data = pd.read_csv('data/StudentsPerformance.csv')
            logging.info('data loaded successfully')
            os.makedirs(os.path.dirname(self.ingestionconfig.RAW_DATA_PATH),exist_ok=True)
            data.to_csv(self.ingestionconfig.RAW_DATA_PATH,index=False,header=True)
            
            logging.info('split ting data into train and test')
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            train_data.to_csv(self.ingestionconfig.TRAIN_DATA_PATH,index=False,header=True)
            test_data.to_csv(self.ingestionconfig.TEST_DATA_PATH,index=False,header=True)
            logging.info('data spliting successfull.')
            
            return(
                self.ingestionconfig.TRAIN_DATA_PATH,
                self.ingestionconfig.TEST_DATA_PATH,
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestionConfig()
    obj.get_data_ingestion_path()