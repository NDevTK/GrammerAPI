# Imports
import os
from deepsegment import DeepSegment
from deepcorrect import DeepCorrect
import flask
from flask import request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
import re

# Great function
def beautify(user_input):
    if not isinstance(user_input, str):
        return "Value not string"
    if len(user_input) > 5000:
        return "Value to big"
    user_input = re.sub(r"[^\w:@!\. (\r\n|\r|\n)]", "", user_input)
    segments = segmenter.segment(user_input)
    result = []
    for segment in segments:
        result.append(corrector.correct(segment)[0]['sequence'])
    return(os.linesep.join(result))

# HTTP Server
app = flask.Flask("GrammarAPI")
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "<title>GrammarAPI</title><h1>GrammarAPI</h1><p>Please send POST request!</p>"

# Fav Endpoint
@app.route('/', methods=['POST'])
def api_main():
    return beautify(request.get_data().decode("utf-8"))

# Deep Stuff
corrector = DeepCorrect('deeppunct_params_en', 'deeppunct_checkpoint_google_news')
segmenter = DeepSegment('en')

# HTTP Server
print("Server Started")
port = int(os.environ.get("PORT", 5000))
http_server = WSGIServer(('0.0.0.0', port), app)
http_server.serve_forever()
