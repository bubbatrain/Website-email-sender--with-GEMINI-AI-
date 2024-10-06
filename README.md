This is a Flask-based project. The website will ask user for:
- an email account;
- a prompt.
The prompt will go through GEMINI AI and the generated response will be sent to the given email account.

-- HOW THIS PROJECT WORKS --
1) The class PromptForm is created to get email and prompt from the user;
2) inside a route called '/' (created for rendering 'home.html' in /templates folder), the app will get email and prompt from user;
3) the AI model (Google Gemini in this case) is configured with the provided API_KEY (see below);
4) the prompt given by the user is given to the AI model and the following response saved;
5) the sender email account is configured with account name and password (see below);
6) the receiver email is set to the email account given by user;
7) the subject and body of the message are configured with the response from AI model;
8) the email is sent.

-- HOW TO MAKE IT WORK --
1) If you use PythonAnywhere to host the app, follow this:
https://help.pythonanywhere.com/pages/Flask/

2) The app uses some environmental variables:
  - "FLASK_SECRET_KEY": "your_flask_key",
  - "API_KEY": "your_google_gemini_key",
  - "SENDER_EMAIL": "your_sender_email@mail.com",
  - "SENDER_PASS": "your_sender_email_password"

In development, you can hardcode this variables in the code/debugger; in production, you need to save the variables in file called '.env' and follow this guide:
https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/
