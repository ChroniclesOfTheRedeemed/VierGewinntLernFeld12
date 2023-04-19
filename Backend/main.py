from src.constants import Api
from src.flask_app import app as application

app = application
Api.Url.base = ""
app.route("/")(lambda: "check it out")

if __name__ == '__main__':
    app.run(threaded=False, processes=1)