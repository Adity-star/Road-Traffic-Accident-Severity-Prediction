import sys
import logging
from dataclasses import dataclass

import pandas as pd
import numpy as np

from source.exception import CustomException
from source.logger import logging

from sklearn.preprocessing import LabelEncoder ,OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


from source.exception import CustomException
from source.logger import logging
import os

from source.utils import save_object

@dataclass

class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprecessor.pkl')

class DataTransformation:

        def __init__(self):

            self.data_transform_config = DataTransformationConfig()

        def drop_unnecessary_columns(self, df, columns_to_drop):
            logging.info(f"Dropping unnecessary columns :{columns_to_drop}")
            df = df.drop(columns=columns_to_drop,errors = 'ignore')

            return df



        def strip_and_lower_columns(self,df):
            """Strip whitespace and convert column names to lowercase"""
            logging.info("Stripping and lowercasing column names.")
            df.columns = df.columns.str.strip().str.lower()

            return df


        def get_data_transformer_object(self,df):
            logging.info("Handling data columns")
            target_column_name = "accident_severity"


            # Drop unnecessary columns before processing the data
            columns_to_drop = ['age_band_of_driver','time','vehicle_driver_relation', 'work_of_casuality', 'fitness_of_casuality','day_of_week','casualty_severity','time','sex_of_driver','educational_level','defect_of_vehicle','owner_of_vehicle','service_year_of_vehicle', 'road_surface_type','sex_of_casualty','age_band_of_casualty','age_band_of_driver']
            columns_to_drop = [col for col in columns_to_drop if col != target_column_name]


            # Get list of numerical and categorical columns
            numerical_columns = df.select_dtypes(include = ['float64', 'int64']).columns.tolist()
            categorical_columns = df.select_dtypes(include = ['object']).columns.tolist()


            #Creating SimpleImputer objects with the appropriate strategies
            simpleimputer_mode = SimpleImputer(strategy = 'most_frequent')
            simpleimputer_mean = SimpleImputer(strategy = 'mean')

            if categorical_columns: 
                df[categorical_columns] = simpleimputer_mode.fit_transform(df[categorical_columns])
            
            
            if numerical_columns:
                df[numerical_columns] = simpleimputer_mean.fit_transform(df[numerical_columns])


            # Creating pipeline for numerical data (Imputation and Scaling)
            numerical_pipeline = Pipeline(
                steps = [
                    ("scaler",StandardScaler())
                ]
            )

            # Creating pipeline for categorical data (Imputation and OneHotEncoding)
            categorical_pipeline = Pipeline(
                steps = [
                    ("onehotencoder",OneHotEncoder(handle_unknown='ignore', sparse_output = False)), # sparse=False for numpy array
                ]
            )

            # Log the columns
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # Combine both pipelines into a single transformer
            preprocessor = ColumnTransformer(
                transformers =  [
                    ("numerical_pipeline",numerical_pipeline,numerical_columns),
                    ("categorical_pipeline",categorical_pipeline,categorical_columns)
                ]
            )

            return preprocessor



        def initiate_data_transformation(self,train_path,test_path):
            try:
                train_df = pd.read_csv(train_path)
                test_df = pd.read_csv(test_path)

                logging.info('Reading train and test data completed')

                logging.info("Obtaining preprocessing object")

                target_column_name = "accident_severity"

                # Separate target before transformation on train data
                logging.info("Splitting the data into features and target")

                input_feature_train_df = train_df.drop(columns = [target_column_name],axis = 1)
                target_feature_train_df = train_df[target_column_name]

                input_feature_test_df = test_df.drop(columns = [target_column_name],axis = 1)
                target_feature_test_df = test_df[target_column_name]

                # Get the preprocessor object
                preprocessing_obj = self.get_data_transformer_object(input_feature_train_df)

                # Transform the input features
                input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
                input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df) # Apply to features only



                logging.info("Applying preprocessing object on training data and testing data")

                train_arr = np.c_[input_feature_train_arr, target_feature_train_df.values.reshape(-1, 1)]  
                test_arr = np.c_[input_feature_test_arr, target_feature_test_df.values.reshape(-1, 1)]

                logging.info('Saved preprocessing object sucessfully')

                save_object (
                    file_path = self.data_transform_config.preprocessor_obj_file_path,
                    obj = preprocessing_obj # Save the preprocessor object
                )

                return (
                    train_arr,
                    test_arr,
                    self.data_transform_config.preprocessor_obj_file_path
                )

            except Exception as e:
                logging.error(f"Error occurred in data transformation: {str(e)}")
                raise CustomException(e,sys)