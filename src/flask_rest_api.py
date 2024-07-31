# Flask REST API to process input URL and return the prediction result

import flask
import json
import numpy as np
import tensorflow as tf

from keras.models import load_model
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

import data_preprocessed


# Initializing the Flask application
app = flask.Flask(__name__)

global tf_graph
tf_graph = tf.compat.v1.get_default_graph()

# Loading the pre-trained model
trained_model = 'malicious_url_detector.h5' # TODO: Fix path, create file
model = load_model(trained_model)

def data_prep(url):
    url_set = data_preprocessed.main()
    sample_set = []
    label_set = []
    
    for key, value in url_set.items():
        sample_set.append(key)
        label_set.append(value)
       
    max_words = 20000
    max_length = 128
    
    # Convert the input URL into sequence of integers 
    # based on the tokenization learned during training
    
    tokenizer = Tokenizer(num_words=max_words, char_level=True)
    tokenizer.fit_on_texts(sample_set)
    sequences = tokenizer.texts_to_sequences(url)
    word_index = tokenizer.word_index
    
    # Padding the sequences and returning the preprocessed data
    url_preprocessed = pad_sequences(sequences, maxlen=max_length)
    return url_preprocessed

@app.route("/predict", methods=["POST"])

def predict():
    
    response = {"success": False} # Initializing the response
    is_base_url = False
    
    if flask.request.method == "POST": # Checking if the request is a POST request
        data_in = flask.request.get_json()
        
        url_set = []
        url = data_in["url"]
        url_set.append(url)
        
        print(url) # Printing the URL to be classified

        url_preprocessed = data_prep(url_set) # Preprocessing the URL
        
        # Making predictions using the pre-trained model
        with tf_graph.as_default():
            predictions = model.predict(url_preprocessed)
            
        print(predictions)
        
        
        response["predictions"] = []
        
        # Setting result based on prediction score
        
        if predictions > 0.50:
            model_result = "The URL provided is likely to be malicious."
        else:
            model_result = "The URL provided is not likely to be malicious."


        # Conduct a check if URL is a base URL
        # Accuracy of the model is low for base URLs
        
        url_split = url.split("//")
        # print(url_split[0])
        url_split2 = url_split[1]
        
        if "/" not in url_split2:
            model_result = "URL is a base URL. Model accuracy is low for base URLs."
            is_base_url = True
            

        # Format prediction for non-base URLs
        predictions = float(predictions)
        predictions = round(predictions, 2) # Round off the prediction score
        predictions = predictions * 100 # Convert to percentage
        
        
        # Formatting the response based on if the URL is a base URL or not
        
        if is_base_url == True:
            returned_prediction = {"Prediction Result": model_result, "URL": url}
        else:
            returned_prediction = {"Prediction Result": model_result, "Malicious URL Probability": str(predictions) + "%", "URL": url}
            
        response["predictions"].append(returned_prediction)
        response["success"] = True # Set request as successful
    
    
    # Return the response as JSON
    return flask.jsonify(response)


# Starting the server
if __name__ == "__main__":
    
    print("* Loading Keras model and Flask starting server...")
    print("* Model loading...") 
    
    app.run(host='0.0.0.0', port=45000)
