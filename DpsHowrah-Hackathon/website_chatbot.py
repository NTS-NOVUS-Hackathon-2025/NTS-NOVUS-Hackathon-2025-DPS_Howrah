from flask import Flask,request,render_template
from chatbot import MODEL

APP= Flask(__name__)


@APP.route('/student/chatbot', methods=['GET', 'POST'])
def getfeedback():
    feedback = None
    if request.method == 'POST':
        # Get the form input data
        text= request.form.get("text")
        
        # Do something with the data (e.g., process it, save it)
        feedback = MODEL.generate_content(text).text
    return render_template('chatbot_result.html', feedback=feedback)

@APP.route("/student/chatbot_result",methods=['GET', 'POST'])
def ret_chatbot():
    if request.method=="POST":
        return render_template("chatbot.html")

if __name__ == '__main__':
    APP.run(debug=True)