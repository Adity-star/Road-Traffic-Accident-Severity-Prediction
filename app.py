from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from source.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__,template_folder = r'C:\Users\Administrator\OneDrive\Desktop\Accident prediction\templates')

app = application

## Route for a home page

@app.route('/')

def index():
    # Load your dataset (update the file path as needed)
    dataset = pd.read_csv(r'C:\Users\Administrator\OneDrive\Desktop\Accident prediction\artifacts\data.csv')

    # Extract unique values from each column
    age_band_of_driver = dataset['age_band_of_driver'].unique().tolist()
    driving_experience = dataset['driving_experience'].unique().tolist()
    type_of_vehicle = dataset['type_of_vehicle'].unique().tolist()
    area_accident_occured = dataset['area_accident_occured'].unique().tolist()
    lanes_or_medians = dataset['lanes_or_medians'].unique().tolist()
    road_allignment = dataset['road_allignment'].unique().tolist()
    types_of_junction = dataset['types_of_junction'].unique().tolist()
    road_surface_conditions = dataset['road_surface_conditions'].unique().tolist()
    light_conditions = dataset['light_conditions'].unique().tolist()
    weather_conditions = dataset['weather_conditions'].unique().tolist()
    type_of_collision = dataset['type_of_collision'].unique().tolist()
    number_of_vehicles_involved = dataset['number_of_vehicles_involved'].unique().tolist()
    number_of_casualties = dataset['number_of_casualties'].unique().tolist()
    vehicle_movement = dataset['vehicle_movement'].unique().tolist()
    casualty_class = dataset['casualty_class'].unique().tolist()
    age_band_of_casualty = dataset['age_band_of_casualty'].unique().tolist()
    pedestrian_movement = dataset['pedestrian_movement'].unique().tolist()

    return render_template('home.html',
                        age_band_of_driver=age_band_of_driver,
                        driving_experience=driving_experience,
                        type_of_vehicle=type_of_vehicle,
                        area_accident_occured=area_accident_occured,
                        lanes_or_medians=lanes_or_medians,
                        road_allignment=road_allignment,
                        types_of_junction=types_of_junction,
                        road_surface_conditions=road_surface_conditions,
                        light_conditions=light_conditions,
                        weather_conditions=weather_conditions,
                        type_of_collision=type_of_collision,
                        number_of_vehicles_involved=number_of_vehicles_involved,
                        number_of_casualties=number_of_casualties,
                        vehicle_movement=vehicle_movement,
                        casualty_class=casualty_class,
                        age_band_of_casualty=age_band_of_casualty,
                        pedestrian_movement=pedestrian_movement)

# Route for predicting 
@app.route('/predictdata',methods=['GET','POST'])

def predict_datapoint():

    if request.method=='GET':
        return render_template('home.html')
    
    else:
        data = CustomData(
            age_band_of_driver=request.form.get('age_band_of_driver'),
            driving_experience=request.form.get('driving_experience'),
            type_of_vehicle=request.form.get('type_of_vehicle'),
            area_accident_occured=request.form.get('area_accident_occured'),
            lanes_or_medians=request.form.get('lanes_or_medians'),
            road_allignment=request.form.get('road_allignment'),
            types_of_junction=request.form.get('types_of_junction'),
            road_surface_conditions=request.form.get('road_surface_conditions'),
            light_conditions=request.form.get('light_conditions'),
            weather_conditions=request.form.get('weather_conditions'),
            type_of_collision=request.form.get('type_of_collision'),
            number_of_vehicles_involved=request.form.get('number_of_vehicles_involved'),
            number_of_casualties=request.form.get('number_of_casualties'),
            vehicle_movement=request.form.get('vehicle_movement'),
            casualty_class=request.form.get('casualty_class'),
            age_band_of_casualty=request.form.get('age_band_of_casualty'),
            pedestrian_movement=request.form.get('pedestrian_movement')
)

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(debug=True)