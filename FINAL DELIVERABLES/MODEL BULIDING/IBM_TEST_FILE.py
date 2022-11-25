import requests

import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "dRe32OTFMluCZqk6qFtDz95jkqS8FbBK4TrAuw7TgqR4"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [[
                                "f0",
                                "f1",
                                "f2",
                                "f3",
                                "f4",
                                "f5",
                                "f6",
                                "f7",
                                "f8",
                                "f9",
                                "f10",
                                "f11",
                                "f12",
                                "f13",
                                "f14",
                                "f15",
                                "f16"
                        ]], "values":[[15, 25.5, 3.7, 4.2, 9.3, 35, 3, 15, 79, 37, 1012.5, 1008.2, 7, 4, 17.6, 27.7, 3.5]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/9f322f69-cea1-4ccb-9a5c-49ec65275698/predictions?version=2022-11-18', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predict = response_scoring.json()
val = (predict['predictions'][0]['values'][0][0])
print(val)