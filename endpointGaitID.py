from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def successfulConnection():
    return "<p>Connection was established successfully!</p>"


@app.route("/addMedia", methods=['POST', "GET"])
def importMedia():
    if request.method == 'POST':
        videoId = request.json['videoId']
        videoUri = request.json['videoUri']

        response = {
            "Recieved Title: ": videoId,
            "Duration of video: ": videoUri
        }

        print("Video uri: ", videoUri, "Video ID: ",videoId)

        return jsonify(response)
    if request.method == "GET":
        return "hola dude"
