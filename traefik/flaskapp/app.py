from flask import Flask
from redis import Redis

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!. I am back"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
