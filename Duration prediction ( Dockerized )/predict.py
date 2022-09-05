import pickle 
from flask import Flask, request, jsonify

with open('lin_reg.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

def preprocessing(ride):
    features = {}
    features['PU_DO'] = f"{ride['PULocationID']}_{ride['DOLocationID']}"
    features['trip_distance'] = ride['trip_distance']
    return features

def predict(features):
    x = dv.transform(features)
    pred = model.predict(x)
    return pred[0]

app = Flask('duration prediction')

@app.route('/')
def home():
    html = f'<h2> Welcome to the home page of Duration Prediction </h2>'
    return html.format(format)

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    json_payload = request.get_json()
    features = preprocessing(json_payload)
    pred = predict(features)
    prediction_json = {
        'duration' : pred
    } 
    return jsonify(prediction_json)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 80)
    
