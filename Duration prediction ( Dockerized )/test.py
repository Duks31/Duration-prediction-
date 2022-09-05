import requests 


ride = {
    'PULocationID' : 10,
    'DOLocationID' : 50,
    'trip_distance' :40
}

# feature_preprocessed = predict.preprocessing(ride)
# prediction = predict.predict(feature_preprocessed)

url  = 'http://localhost:80/predict'
response = requests.post(url, json=ride)
print(response.json())



