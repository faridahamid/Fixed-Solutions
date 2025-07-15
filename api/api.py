import pickle
import flask
from flask import request
from sklearn.linear_model import LogisticRegression

app = flask.Flask(__name__)
with open("iris_model.pkl", 'rb') as file:  
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    
    feature_array = request.get_json()['feature_array']

   
    prediction = model.predict([feature_array]).tolist()
    

    response = {}
    response['prediction'] = prediction
    

    return flask.jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port ='5000',host='0.0.0.0')