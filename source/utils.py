import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RepeatedStratifiedKFold, GridSearchCV
from source.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    acc_result = {}

    try:

        for model_name, model in models.items():            

            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = accuracy_score(y_train, y_train_pred)
            test_model_score = accuracy_score(y_test, y_test_pred)

            acc_result[model_name] = test_model_score

        return acc_result 
    
    except Exception as e:
        raise CustomException(e, sys)

    
def best_model(result):
    high = 0
    model_name = None
    for name, acc in result.items():
        if acc > high:
            high = acc
            model_name = name
    return model_name

def best_params(model, param, X_train, y_train):
    try:
        # Define cross-validation strategy
        cv = RepeatedStratifiedKFold(n_splits = 5, n_repeats = 2, random_state = 42)

        grid_cv = GridSearchCV(estimator = model, param_grid = param, cv = cv, scoring = "accuracy")  # scoring="accuracy" for classification
        res = grid_cv.fit(X_train, y_train)

        return res.best_params_

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)

