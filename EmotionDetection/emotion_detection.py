import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)

    if response.status_code == 400:
        final_output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        json_response = json.loads(response.text)
        final_output = json_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(final_output, key=final_output.get)
        final_output['dominant_emotion'] = dominant_emotion
    return final_output    