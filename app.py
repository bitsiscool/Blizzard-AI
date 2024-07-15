from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Replace 'YOUR_APP_ID' with your actual WolframAlpha API key
WOLFRAMALPHA_APP_ID = '8HUP3L-RW9H6TXQP5'

def ask_wolframalpha(query):
    url = f"http://api.wolframalpha.com/v1/result?appid={WOLFRAMALPHA_APP_ID}&i={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "I couldn't understand the question."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    query = request.form['query']
    answer = ask_wolframalpha(query)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
