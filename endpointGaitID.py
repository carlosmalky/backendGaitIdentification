from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def successfulConnection():
    return "<p>Connection was established successfully!</p>"


@app.route("/addMedia", methods=['POST'])
def importMedia():
    if request.method == 'POST':
        videoTitle = request.form['videoTitle']
        videoDuration = request.form['videoDuration']
        response = {
            "Recieved Title: ": videoTitle,
            "Duration of video: ": videoDuration
        }
        return jsonify(response)
