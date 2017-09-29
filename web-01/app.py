from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Flask Dockerized on  " + datetime.today().isoformat()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')