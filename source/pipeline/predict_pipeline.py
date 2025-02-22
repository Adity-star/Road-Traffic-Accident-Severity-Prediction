import sys
import pandas as pd
from source.exception import CustomException
from source.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try :
            model_path = os.path.join("artifacts","model.pkl")

            preprocessor_path = (r'C:\Users\Administrator\OneDrive\Desktop\Accident prediction\artifacts\preprecessor.pkl')
            print("Before Loading")

            model=load_object(file_path = model_path)
            preprocessor=load_object(file_path = preprocessor_path)

            print("After Loading")

            data_scaled = preprocessor.transform(features)
            return model.predict(data_scaled)
        
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:

    def __init__(  self,
        
        age_band_of_driver : str,
        driving_experience: str,
        type_of_vehicle: str,
        area_accident_occured: str,
        road_allignment: str,
        types_of_junction: int,
        road_surface_conditions: int,
        light_conditions:str,
        weather_conditions:str,
        type_of_collision:str,
        number_of_vehicles_involved:int,
        number_of_casualties:int,
        pedestrian_movement:str,
        age_band_of_casualty:str,
        casualty_class:str,
        vehicle_movement:str,
        lanes_or_medians:int
        ):

        self.age_band_of_driver = age_band_of_driver

        self.driving_experience = driving_experience

        self.type_of_vehicle = type_of_vehicle

        self.area_accident_occured = area_accident_occured

        self.lanes_or_medians = lanes_or_medians

        self.road_allignment = road_allignment

        self.types_of_junction = types_of_junction

        self.road_surface_conditions = road_surface_conditions

        self.light_conditions = light_conditions

        self.weather_conditions =  weather_conditions

        self.type_of_collision = type_of_collision

        self.number_of_vehicles_involved = number_of_vehicles_involved

        self.number_of_casualties = number_of_casualties

        self.vehicle_movement = vehicle_movement

        self.casualty_class = casualty_class
        
        self.age_band_of_casualty = age_band_of_casualty

        self.pedestrian_movement =pedestrian_movement



    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age_band_of_driver": [self.age_band_of_driver],
                "driving_experience": [self.driving_experience],
                "type_of_vehicle": [self.type_of_vehicle],
                "area_accident_occured": [self.area_accident_occured],
                "lanes_or_medians =": [self.lanes_or_medians],
                "road_allignment": [self.road_allignment],
                "types_of_junction": [self.types_of_junction],
                "road_surface_conditions": [self.road_surface_conditions],
                "light_conditions =": [self.light_conditions],
                "weather_conditions": [self.weather_conditions],
                "type_of_collision": [self.type_of_collision],
                "number_of_vehicles_involved": [self.number_of_vehicles_involved],
                "number_of_casualties =": [self.number_of_casualties],
                "vehicle_movement": [self.vehicle_movement],
                "casualty_class": [self.casualty_class],
                "age_band_of_casualty": [self.age_band_of_casualty],
                "pedestrian_movement": [self.pedestrian_movement]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
