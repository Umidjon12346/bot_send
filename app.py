from flask import Flask,request
import telegram

Token = "6745554947:AAH0Xt-pNF7dasRCeI2BjgMuXN-1o-DzFbk"
bot = telegram.Bot(Token)
chat_id = "1806482236"
app = Flask(__name__)

@app.route("/",methods = ["POST"])
def user():
    data = request.get_json()
    bot.send_message(chat_id=data['message']['chat']['id'],text=data['message']['text'])
    return "HEllo"

if __name__=="__main__":
    app.run(debug=True)   