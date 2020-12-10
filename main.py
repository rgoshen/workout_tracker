import os
import requests

API_KEY = os.environ.get("NUTX_API_KEY")
APP_ID = os.environ.get("NUTX_APP_ID")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

def convert_to_kg(weight):
    """Takes in a weight string and returns a weight in kg."""
    weight_text_split = weight.split()
    number = int(weight_text_split[0])
    units = weight_text_split[1]
    
    if units == "lbs":
        kg = number * 0.453592
    else:
        kg = number
        
    return kg
    
    
def convert_to_cm(height):
    """Takes in a height string and returns a height in cm."""
    height_text_split = height.split()
    number = int(height_text_split[0])
    units = height_text_split[1]
    
    if units == "m":
        cm = number * 100
    else:
        cm = number
        
    return cm

# user input
gender_text = input('Are you "male" or "female": ')
weight_text = input('What is your weight? (Ex. "100 kg" or "180 lbs"): ')
height_text = input("What is your height? (Ex. 1.5 m, 150 cm): ")
age_text = int(input("How old are you? "))
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,    
}

parameters = {
    "query": exercise_text,
    "gender": gender_text,
    "weight_kg": convert_to_kg(weight_text),
    "height_cm": convert_to_cm(height_text),
    "age": age_text
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
