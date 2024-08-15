"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection.

Author(Learner): Divya Mahajan

"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask ("Emotion Detection")

@app.route('/emotionDetector')
def emotion_detection_function():
    """
    Analyze the text for emotions and return the result.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyse)

    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {res['anger']} "
        f"'disgust': {res['disgust']}, 'fear': {res['fear']}, "
        f"'joy': {res['joy']} and 'sadness': {res['sadness']}. "
        f"The dominant emotion is {res['dominant_emotion']}."
    )

@app.route('/')
def render_page():
    """
    Render the html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
