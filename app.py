    # Website ask user for:
    #   - an email account;
    #   - a prompt.
    #
    # The prompt will go through GEMINI AI and the response will be
    # send to the given email account.


import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator
import google.generativeai
import smtplib
import ssl
from email.message import EmailMessage 



# Flask app configurations
app = Flask(__name__)
# Set secret key
app.secret_key = os.getenv("FLASK_SECRET_KEY")
# Create app
bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)


# Class for styling the form
class PromptForm(FlaskForm):
    # Fields of the Form
    email = EmailField("Email:", validators=[Email(), DataRequired()])
    prompt = StringField("Prompt:", validators=[DataRequired()], render_kw={"style": "width: 80%"})
    submit = SubmitField("Submit")


# Homepage routing
@app.route("/", methods = ["GET", "POST"])
def home():
    # Create form
    form = PromptForm()

    # If POST method (when user Submit the form)
    if form.validate_on_submit():
        # Get data from form
        receiver_email = form["email"].data
        prompt = form["prompt"].data

        # --------- AI PROMPT REQUEST ---------

        # Configure AI model with API KEY
        google.generativeai.configure(api_key=os.getenv("API_KEY"))

        # Select AI model to use
        model = google.generativeai.GenerativeModel('gemini-1.5-flash')

        # Generate content from the given prompt
        response = model.generate_content(prompt)


        # --------- EMAIL SENDING ---------
        # Sender email details
        SENDER_EMAIL = os.getenv("SENDER_EMAIL")
        SENDER_PASS = os.getenv("SENDER_PASS")
        
        # Receiver email details from the given email
        RECEIVER_EMAIL = receiver_email

        # Subject of email
        subject = "Your AI response is here"

        # Body of email, formatted
        body = response.text.replace("**", "")

        # Configure email
        msg = EmailMessage()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject
        msg.set_content(body)

        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as server:
            server.login(SENDER_EMAIL, SENDER_PASS)
            server.send_message(msg)

    # Render page
    return render_template("home.html", form=form)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
