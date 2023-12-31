
from flask import Flask, render_template, jsonify
import json
import html

app = Flask(__name__)

# Hello World Endpoint
@app.route('/api')
def hello_world():
    data = {'message': 'Hello, world!'}
    response = jsonify(data)
    return response

# Healthcheck Endpoint
@app.route('/health')
def healthcheck():
    return jsonify({'status': 'ok'})

@app.route('/')
#def index():
#    return render_template('index.html', title="page", jsonfile=json.dumps(data))

def index():
    with open('index.html', 'r') as file:
        content = file.read()
    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0')
