# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin

from user_management import UserManagement

app = Flask(__name__)
CORS(app)

email = "username"
password = "password"
user_manager = UserManagement()


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    if request.method == 'POST':
        x = request.json
        print(x)

        if email in x and password in x:
            result = user_manager.login(x[email], x[password])
        else:
            result = "bad request"
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/create_users', methods=['POST'])
def logina():
    if request.method == 'POST':
        x = request.json
        print(x)
        if email in x and password in x:
            return user_manager.add_user(x[email], x[password])
        return "bad request"


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
