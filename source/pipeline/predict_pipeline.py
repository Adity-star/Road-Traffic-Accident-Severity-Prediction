import sys
import pandas as pd
from source.exception import CustomException
from source.utils import load_object
import json
import os

class PredictPipeline:
    def __init__(self):
        # Load paths from configuration file
        with open('config.json', 'r') as config_file:
            self.config = json.load(config_file)
        
        self.model_path = self.config['model_path']
        self.preprocessor_path = self.config['preprocessor_path']

    def predict(self, features):
        try:
            print("Before Loading")
            # Load model and preprocessor
            model = load_object(file_path=self.model_path)
            preprocessor = load_object(file_path=self.preprocessor_path)
            print("After Loading")

            # Ensure prediction data has the same columns as training data
            training_columns = list(preprocessor.feature_names_in_)
            features = features.reindex(columns=training_columns, fill_value=0)

            # Scale the data using the preprocessor
            data_scaled = preprocessor.transform(features)

            # Return the prediction
            return model.predict(data_scaled)
        
        except Exception as e:
            raise CustomException(f"Error during prediction: {str(e)}")

class CustomData:
    def __init__(self, data: dict):
        self.driving_experience = data.get("driving_experience")
        self.type_of_vehicle = data.get("type_of_vehicle")
        self.area_accident_occured = data.get("area_accident_occured")
        self.road_allignment = data.get("road_allignment")
        self.types_of_junction = data.get("types_of_junction")
        self.road_surface_conditions = data.get("road_surface_conditions")
        self.light_conditions = data.get("light_conditions")
        self.weather_conditions = data.get("weather_conditions")
        self.type_of_collision = data.get("type_of_collision")
        self.number_of_vehicles_involved = data.get("number_of_vehicles_involved")
        self.number_of_casualties = data.get("number_of_casualties")
        self.pedestrian_movement = data.get("pedestrian_movement")
        self.age_band_of_casualty = data.get("age_band_of_casualty")
        self.casualty_class = data.get("casualty_class")
        self.vehicle_movement = data.get("vehicle_movement")
        self.lanes_or_medians = data.get("lanes_or_medians")

    def get_data_as_data_frame(self):
        try:
            # Create a dictionary with the values directly
            custom_data_input_dict = {
                "driving_experience": self.driving_experience,
                "type_of_vehicle": self.type_of_vehicle,
                "area_accident_occured": self.area_accident_occured,
                "lanes_or_medians": self.lanes_or_medians,
                "road_allignment": self.road_allignment,
                "types_of_junction": self.types_of_junction,
                "road_surface_conditions": self.road_surface_conditions,
                "light_conditions": self.light_conditions,
                "weather_conditions": self.weather_conditions,
                "type_of_collision": self.type_of_collision,
                "number_of_vehicles_involved": self.number_of_vehicles_involved,
                "number_of_casualties": self.number_of_casualties,
                "vehicle_movement": self.vehicle_movement,
                "casualty_class": self.casualty_class,
                "age_band_of_casualty": self.age_band_of_casualty,
                "pedestrian_movement": self.pedestrian_movement
            }

            # Return data as a pandas DataFrame
            return pd.DataFrame([custom_data_input_dict])
        
        except Exception as e:
            raise CustomException(f"Error while converting data to DataFrame: {str(e)}")