from src.constants import Api
from src.flask_app import app

Api.Url.base = ""

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()