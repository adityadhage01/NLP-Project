from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)


@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    translated = translator.translate(data['text'], dest=data['language'])
    return jsonify({'translated_text': translated.text})

if __name__ == '__main__':
    app.run(debug=True)
