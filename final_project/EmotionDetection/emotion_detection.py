import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        keys = list(emotions.keys())
        scores = list(emotions.values())
        max_index = scores.index(max(scores)) 
        max_emotion = keys[max_index]
        emotions["dominant_emotion"] = max_emotion
    elif response.status_code == 400:
        emotions = {}
        emotions["anger"] = None
        emotions["disgust"] = None
        emotions["fear"] = None
        emotions["joy"] = None
        emotions["sadness"] = None
        emotions["dominant_emotion"] = None
    return emotions
