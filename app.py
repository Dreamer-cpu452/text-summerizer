from flask import Flask, render_template, request, jsonify
from summarizer import generate_summary

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():

    data = request.get_json()

    text = data.get('text', '')

    ratio = data.get('ratio', 0.6)

    summary = generate_summary(
        text,
        float(ratio)
    )

    return jsonify({
        'summary': summary
    })

if __name__ == '__main__':
    app.run(debug=True)