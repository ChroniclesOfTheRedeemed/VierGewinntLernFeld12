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
        print(x)
        if email in x and password in x:
            print("it's there")
            if x[email] == "admin" and x[password] == "admin":
                return  "authentication succeeded"
            else:
                return "authentication failed"
        return "bad request"


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
