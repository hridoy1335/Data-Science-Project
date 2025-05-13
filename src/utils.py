import os
import sys
import pickle
from src.logger import logging
from src.exception import CustomException


def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
            logging.info(f"Object saved successfully at {file_path}")
    except Exception as e:
        raise CustomException(e,sys)
