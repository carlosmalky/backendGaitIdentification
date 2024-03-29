from flask import Flask, request, jsonify
import base64
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

# Command to run program
# flask --app endpointGaitID --debug run -h 192.168.1.144 //Puritan
# flask --app endpointGaitID --debug run -h 192.168.0.167 //Doomsday
# 10.35.39.180 - specific to computer
# https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network


@app.route("/")
def successfulConnection():
    return "<p>Connection was established successfully!</p>"

@app.route("/base64Endpoint", methods=['POST','GET'])
def base64Endpoint():
    if request.method == 'POST':
        videoBase64 = request.json['videoBase64']
        videoUri = request.json["videoUri"]

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

    with open("./Assets/returned_person.jpeg", "rb") as image2string:
        imageBase64 = base64.b64encode(image2string.read())

    response = {
        'userFound' : 'true',
        'userImageBase64': str(imageBase64),
        'userVideoBase64' : str(video),
        'userName':'Akeem Malky',
        'userID':"010876853",
    }
    return response

if __name__ == '__main__':
    print("Backend running!")
    app.run(debug=True)