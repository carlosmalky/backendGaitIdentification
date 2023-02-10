from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def successfulConnection():
    return "<p>Connection was established successfully!</p>"

@app.route("/base64Endpoint", methods=['POST','GET'])
def base64Endpoint():
    if request.method == 'POST':
        videoBase64 = request.json['videoBase64']
        videoUri = request.json["videoUri"]
        # print("Video Base64: ", videoBase64)
        print("bas64 endpoint reached succesfully")

        f = open("base64.txt", "w")
        f.write(videoBase64)
        f.close()

        personIdentity = personIdentification(videoBase64)
        return personIdentity


@app.route("/videoEndpoint", methods=['POST','GET'])
def videoEndpoint():
    if request.method == 'POST':
        videoData = request.files['video']
        
        response = {
            'status': 'success',
            'video_duration': 'video_duration'
        }
        print(response)
        return response

@app.route("/addMedia", methods=['POST', "GET"])
def importMedia():
    if request.method == 'POST':
        videoId = request.json['videoId']
        videoUri = request.json['videoUri']

        response = {
            "Video ID: ": videoId,
            "Video URI: ": videoUri
        }

        print(response)

        return response

    if request.method == "GET":
        return "hola dude"


def personIdentification(video):
    response = {
        'userFound' : 'true',
        'userName':'Akeem',
        'userID':"001",
    }
    return response