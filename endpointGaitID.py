from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def successfulConnection():
    return "<p>Connection was established successfully!</p>"


@app.route("/addMedia", methods=['POST', "GET"])
def importMedia():
    if request.method == 'POST':
        videoTitle = request.json['videoTitle']
        videoDuration = request.json['videoDuration']

        response = {
            "Recieved Title: ": videoTitle,
            "Duration of video: ": videoDuration
        }

        print(videoDuration, videoTitle)

        return jsonify(response)
    if request.method == "GET":
        return "hola dude"
