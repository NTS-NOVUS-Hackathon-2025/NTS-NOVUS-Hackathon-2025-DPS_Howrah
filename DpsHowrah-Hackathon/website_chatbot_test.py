from flask import Flask
from chatbot import MODEL

APP= Flask(__name__)

@APP.route("/ai_help/<prompt>")
def ai_help(prompt):
    message= MODEL.generate_content(prompt).text.replace("\n","<br>")
    return f"<h1> The response: </h1> <br><br> <p> {message} <p>"

if __name__=="__main__":
    APP.run()
