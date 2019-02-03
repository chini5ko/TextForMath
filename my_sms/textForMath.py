from flask import Flask, request, redirect, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.config.from_object(__name__)

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
        resp.message("What's 10 + 1?")
    elif body == '2':
        resp.message("What's 20 - 1?")
    elif body == '3':
        resp.message("What's 30 * 2?")
    elif body == '11':
        resp.message("That's Correct! \nPress Math for menu \nor Press 1 for one more")
    elif body == '19':
        resp.message("That's Correct! \nPress Math for menu \nor Press 2 for one more")
    elif body == '60':
        resp.message("That's Correct! \nPress Math for menu \nor Press 3 for one more")
    elif body.isalpha():
        resp.message("Not a number")
    elif body.isdigit():
        resp.message("Incorrect, try again!")
    else:
        resp.message("Sorry, we did not undestand that, try again with:")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)