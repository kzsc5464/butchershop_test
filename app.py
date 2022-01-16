import requests
import json

# from flask import Flask, render_template

#  API_인증키
API = "687361594d6b7a633636674658504b"



url = "http://openapi.seoul.go.kr:8088/687361594d6b7a633636674658504b/json/LOCALDATA_072206/1/100/"
response = requests.get(url)
contents = response.text
json_Ob = json.loads(contents)


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

if __name__=="__main__":
    # app.run(debug=True)

    index = 0
    while(index < 100):
        print(json_Ob["LOCALDATA_072206"]["row"][index]["SITEWHLADDR"])
        print(json_Ob["LOCALDATA_072206"]["row"][index]["DTLSTATENM"])
        index += 1
        print(index)