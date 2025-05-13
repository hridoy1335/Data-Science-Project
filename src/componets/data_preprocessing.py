import os
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.exception import CustomException
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder


@dataclass
class DataPreproccessingConfig():
    """Data Preprocessing configuration class"""
    model_object_file_path = os.path.join('artifacts','model.pkl')
    
class DataPreprocessing:
    def __init__(self):
        self.data_transformation_config = DataPreproccessingConfig()
        
    def get_data_transformer_object(self):
        """This function returns the data transformer object"""
        try:
            numerical_columns = [
                'math score',
                'reading score',
                'writing score'
            ]
            
            categorical_columns = [
                'gender',
                'ethnicity',
                'edu_level',
                'lunch',
                'course'
            ]
            
            pipe_numerical = Pipeline(
                steps = [
                    'impute', SimpleImputer(strategy='mean'),
                    'scaler', StandardScaler()
            ])
            
            pipe_categorical = Pipeline(
                steps=[
                'impute', SimpleImputer(strategy='most_frequent'),
                'encoder', OneHotEncoder(handle_unknown='ignore')
            ])
            
            logging.info(f"numerical_columns:->{numerical_columns}")
            logging.info(f"categorical_columns:->{categorical_columns}")
            
            preprocessor = ColumnTransformer(
                [
                    ("nam_columns", pipe_numerical, numerical_columns),
                    ("cat_columns", pipe_categorical, categorical_columns)
                ],
                remainder='passthrough',
                n_jobs= -1)
            
            logging.info('make columns transformer object created')
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        """This function initiates the data transformation process"""
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            
            logging.info('file read successfully')
            
            preproccessing_obj = self.get_data_transformer_object()
            
            logging.info('spliting feature columns and terget columns')
            
            target_columns_name = "avg_score"
            
            input_feature_train_data = train_data.drop([target_columns_name],axis=1)
            target_train_data = train_data[target_columns_name]
            
            input_feature_test_data = test_data.drop([target_columns_name],axis=1)
            target_test_data = test_data[target_columns_name]
            
            logging.info('applying preprocessor traing data and test data')
            
            input_feature_train_array = preproccessing_obj.fit_transform(input_feature_train_data)
            input_feature_test_array = preproccessing_obj.transform(input_feature_test_data)
            
            train_array = np.c_[input_feature_train_array,np.array(target_train_data)]
            test_array = np.c_[input_feature_test_array,np.array(target_test_data)]
            
            logging.info('save model object')
            
            save_object(
                file_path = self.data_transformation_config.model_object_file_path,
                obj = preproccessing_obj
            )
            
            return(
                train_array,
                test_array,
                self.data_transformation_config.model_object_file_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
    
