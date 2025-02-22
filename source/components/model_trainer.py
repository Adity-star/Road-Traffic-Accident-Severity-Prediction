import os
import sys

from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler,MinMaxScaler,LabelEncoder
from sklearn.model_selection import RepeatedStratifiedKFold,GridSearchCV
from sklearn.model_selection import KFold 
from sklearn.metrics import accuracy_score

from source.exception import CustomException
from source.logger import logging


from source.utils import save_object,evaluate_models,best_model,best_params

@dataclass

class ModelTrainerConfig():

    trained_model_file_path = os.path.join("artifacts",'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        logging.info("Spliting the dataset into train and tests sets")


        acc_result = {}

        X_train, y_train, X_test, y_test = (
            train_array[:, :-1], 
            train_array[:, -1], 
            test_array[:, :-1], 
            test_array[:, -1]
        )
        
        models={
            "LogisticRegression":LogisticRegression(),
            "DecisionTreeClassifier":DecisionTreeClassifier(),
            "KNeighborsClassifier":KNeighborsClassifier(),
            "GNB":GaussianNB(),
            "RandomForestClassifier":RandomForestClassifier(),
            "AdaBoostClassifier":AdaBoostClassifier(),
            "GradientBoostingClassifier":GradientBoostingClassifier(),
        }

        model_report:dict = evaluate_models(X_train = X_train,y_train = y_train,X_test = X_test,y_test = y_test,
                                            models = models)
        
        # Collect results in acc_result
        for model_name, model_acc in model_report.items():
            acc_result[model_name] = model_acc

        logging.info(f"Model evaluation completed. Results: {acc_result}")

        # Determine best model and its parameters
        best_model_name = best_model(acc_result) 
        best_model_instance = models[best_model_name] 

        # Get parameter grid for the best model
        param_grids = self.get_param_grid_for_model(best_model_name)

        # Perform Grid Search to find the best parameters
        grid_search = GridSearchCV(estimator = best_model_instance, param_grid = param_grids, 
                                cv = 5, scoring='accuracy', n_jobs = -1)
        grid_search.fit(X_train, y_train)

        # Get the best parameters and model
        best_params = grid_search.best_params_
        logging.info(f"Best parameters for {best_model_name}: {best_params}")

        
        # Retrain the best model with the optimal parameters
        best_model_instance.set_params(**best_params)
        best_model_instance.fit(X_train, y_train)
        
        # Evaluate the tuned model
        y_pred = best_model_instance.predict(X_test)
        tuned_accuracy = accuracy_score(y_test, y_pred)

        logging.info(f"Tuned {best_model_name} accuracy: {tuned_accuracy}") 

        # Save the best model
        save_object(
            file_path = self.model_trainer_config.trained_model_file_path,
            obj = best_model_instance
        )

        return  tuned_accuracy
        
    def get_param_grid_for_model(self, model_name):

        # Define parameter grids for each model (this is an example; you can adjust as necessary)
        param_grids = {
            "LogisticRegression": {
                "C": [0.1, 1, 10],
                "solver": ['liblinear', 'lbfgs'],
            },
            "DecisionTreeClassifier": {
                "max_depth": [None, 10, 20, 30],
                "min_samples_split": [2, 5, 10],
            },
            "SVM": {
                "C": [0.1, 1, 10],
                "kernel": ['linear', 'rbf'],
            },
            "KNeighborsClassifier": {
                "n_neighbors": [3, 5, 7, 9],
                "weights": ['uniform', 'distance'],
            },
            "RandomForestClassifier": {
                "n_estimators": [100, 200],
                "max_depth": [None, 10, 20],
                "min_samples_split": [2, 5],
            },
            "AdaBoostClassifier": {
                "n_estimators": [50, 100],
                "learning_rate": [0.01, 0.1, 1],
            },
            "GradientBoostingClassifier": {
                "n_estimators": [100, 200],
                "learning_rate": [0.01, 0.1],
                "max_depth": [3, 5],
            }
        }
        return param_grids.get(model_name, {})
            




