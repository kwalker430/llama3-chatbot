from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

# Global variable to keep track of conversation history
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history

    user_message = request.json.get('message')

    # Append the user's message to the conversation history
    conversation_history.append({'role': 'user', 'content': user_message})

    # Call the ollama chat model
    response = ollama.chat(model='llama3', messages=conversation_history, stream=False)
    print(response)

    # Get the AI response and add it to the conversation history
    response_text = response['message']['content']
    conversation_history.append({'role': 'assistant', 'content': response_text})

    return jsonify({'response': response_text})

@app.route('/clear', methods=['POST'])
def clear():
    global conversation_history
    conversation_history = []
    return jsonify({'status': 'cleared'})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
