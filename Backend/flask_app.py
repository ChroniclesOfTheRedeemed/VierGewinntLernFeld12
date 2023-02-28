# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

email = "username"
password = "password"

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        x = request.json
        if email in x and password in x:
            if x[email] == "admin" and x[password] == "admin":
                return "authentication succeeded"
        return "authentication failed"



if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
