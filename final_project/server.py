''' This is a server for emotion detection.'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This function takes the input text and gives the detection output.'''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant = response["dominant_emotion"]
    if dominant is None:
        return "Invalid text! Please try again!"
    return ("For the given statement, the system response is 'anger': " f"{anger}"
    ", 'disgust': " f"{disgust}" ", 'fear': " f"{fear}" ", 'joy': " f"{joy}"
    ", 'sadness': " f"{sadness}" ". The dominant emotion is " f"{dominant}" ".")

@app.route("/")
def render_page():
    ''' This function renders the html page.'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
