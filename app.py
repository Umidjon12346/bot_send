from flask import Flask,request
import telegram

app = Flask(__name__)

@app.route("/")
def user():
    return "HEllo"

if __name__=="__main__":
    app.run(debug=True)   