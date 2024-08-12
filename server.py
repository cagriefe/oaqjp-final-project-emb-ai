from flask import Flask, request, render_template
from EmotionDetector.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=['GET', 'POST'])
def emo_detector():
    """
    Handle the emotion detection request.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please provide text to analyze."
    
    result = emotion_detector(text_to_analyze)
    if result is None:
        return "Unable to detect emotion. Please try again!"
    
    return f"For the given statement, the detected emotion is: {result}"

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)