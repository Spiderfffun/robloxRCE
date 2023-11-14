from flask import Flask, request, jsonify
import os
import subprocess
app = Flask(__name__)
def execute(content):
    try:
        cmdoutput = subprocess.check_output(content, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        cmdoutput = e.output
    except Exception as e:
        return e
    try:
        cmdoutput = cmdoutput.decode()
    except:
        try:
            return cmdoutput
        except Exception as e:
            return e
    else:
        return cmdoutput

@app.route('/', methods=['POST'])
def receive_data():
    content = request.form.get('content')
    cmd = execute(content)

    print(f"Received data from Roblox: {content}")

    return jsonify({'response': cmd})

if __name__ == '__main__':
    app.run(debug=True, port = 3000)
