import os
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.exception import CustomException
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    TRAIN_DATA_PATH:str = os.path.join('artifacts','train_data.csv')
    TEST_DATA_PATH:str = os.path.join('artifacts','test_data.csv')
    RAW_DATA:str = os.path.join('artifacts','raw.csv')
    
class Dataingestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    def initiate_data_config(self)->pd.DataFrame:
        logging.info('data ingestion started...')
        try:
            logging.info('loading data set.')
            df = pd.read_csv('/Users/mac/Developer/Data Science Project/data/customer_training_dataset.csv')
            df = df.iloc[:,1:]
            logging.info('data loaded successfull')
            os.makedirs(os.path.dirname(self.data_ingestion_config.RAW_DATA),exist_ok=True)
            df.to_csv(self.data_ingestion_config.RAW_DATA,index=False,header=True)
            logging.info('raw data was sent the artifacts folder successfully.')
            
            logging.info('spling the file to train and test')
            train_data, test_data = train_test_split(df,test_size=0.2,random_state=42)
            logging.info('split data train and test sucessfully.')
            
            train_data.to_csv(self.data_ingestion_config.TRAIN_DATA_PATH,index=False,header=True)
            test_data.to_csv(self.data_ingestion_config.TEST_DATA_PATH,index=False,header=True)
            logging.info('train and test file sent the artifacts folder successfully.')
            
            return(
                train_data,
                test_data
            )
                        
        except Exception as e:
            raise CustomException(e,sys) from e
        
if __name__ == "__main__":
    obj = Dataingestion()
    obj.initiate_data_config()