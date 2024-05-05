from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/submit-voice-input', methods=['POST'])
def receive_voice_input():
  data = request.get_json()
  user_input = data.get('user_input')
  print(data)
  return jsonify({'message': 'Received input successfully!'})

if __name__ == '_main_':
    app.run(debug=True)