from flask import Flask,jsonify
from getConnectedHosts import getActiveHosts
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def summary():
	d = getActiveHosts()
	return jsonify(d)

if __name__ == "__main__":
    app.run(host="192.168.1.138")