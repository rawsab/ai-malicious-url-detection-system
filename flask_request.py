import argparse
import requests
import json

def main(url):
    
    KERAS_REST_API_URL = "http://localhost:45000/predict" # Defining API endpoint URL
    client_data = {"url": url} # Setting data to JSON format
    
    req = requests.post(KERAS_REST_API_URL, json=client_data) # Sending the POST request
    api_response = req.json() # Getting the response from the server
    
    # Returning predictions if request is successful
    if api_response["success"]:
        print("Predictions:", api_response['predictions'])
    else:
        print("Request to server failed.")
        

if __name__ == "__main__":
    # Command-line argument parser
    cl_parser = argparse.ArgumentParser()
    cl_parser.add_argument('-u', dest='url', action='store', required=True, help="URL to be classified.")
    arguments = cl_parser.parse_args()
    
    # Calling main with command-line arguments from parser
    main(**vars(arguments))