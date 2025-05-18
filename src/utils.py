import os
import sys
import pickle
from src.logger import logging
from src.exception import CustomException


def save_object(filepath,obj):
    try:
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath,'wb') as file:
            pickle.dump(obj,file)
            logging.info('pikle file created successfull')
    except Exception as e:
        raise CustomException(e,sys) from e