from flask import Flask, request, redirect, session
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)
app.config.from_object(__name__)

def addition():
    x =  random.randint(1,6)
    question = ""
    # Start our TwiML response
    print(x)
    x = str(x)
    if x == '1':
        question = "What's 2000 + 19?"
    elif x == '2':
        question = "What's 22 + 24?"
    elif x == '3':
        question = "What's 70 + 40?"
    elif x == '4':
        question = "What's 345 + 67?"
    elif x == '5':
        question = "What's 350 + 350?"    
    else:
        question = "What's 63 + 8?"
    
    return str(question)

def substraction():
    x =  random.randint(1,6)
    question = ""
    # Start our TwiML response
    print(x)
    x = str(x)
    if x == '1':
        question = "What's 125 - 100?"
    elif x == '2':
        question = "What's 57 - 5?"
    elif x == '3':
        question = "What's 90 + 9?"
    elif x == '4':
        question = "What's 75-50?"
    elif x == '5':
        question = "What's 83-31?"    
    else:
        question = "What's 91 - 10?"
    
    return str(question)
    
def correct():
    return str("that's Correct! \nPress Math for menu \nor Press 1 for one more")


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None).lower()

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    # Menu = count=0
    if body == 'menu':
        resp.message("Press # for \n" +
        "1 - Addition \n" +
        "2 - Substraction \n"
        "3 - Multiplication")
    elif body == 'math':
        resp.message("Press # for \n" +
        "1 - Addition \n" +
        "2 - Substraction \n"
        "3 - Multiplication")
    elif body == '1':
        resp.message(addition())
    elif body == '2':
        resp.message(substraction())
    elif body == '3':
        resp.message(substraction())
    elif body == '2019':
        resp.message(correct())
    elif body == '56':
        resp.message(correct())
    elif body == '71':
        resp.message(correct())
    elif body == '110':
        resp.message(correct())
    elif body == '412':
        resp.message(correct())
    elif body == '700':
        resp.message(correct())
    elif body == '25':
        resp.message(correct())
    elif body == '52':
        resp.message(correct())
    elif body == '81':
        resp.message(correct())
    elif body.isalpha():
        resp.message("Sorry, we did not undestand that. \nPlease type: \nMenu")
    elif body.isdigit():
        resp.message("Incorrect, try again!")
    else:
        resp.message("Sorry, we did not undestand that, try again with:")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


