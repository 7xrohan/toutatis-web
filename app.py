from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/run', methods=['POST'])
def run_toutatis():
    data = request.get_json()
    username = data.get('username')
    sessionid = data.get('sessionid')

    if not username or not sessionid:
        return jsonify({'error': 'Username and session ID are required'}), 400

    try:
        result = subprocess.check_output(
            ['toutatis', '-u', username, '-s', sessionid],
            stderr=subprocess.STDOUT,
            text=True
        )
        return jsonify({'output': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output}), 500

# 👇 THIS BLOCK IS REQUIRED TO START THE SERVER
if __name__ == '__main__':
    app.run(debug=True, port=5000)
