from flask import Flask, render_template

ALLOWED_EXTENSIONS = ['img', 'jpg']

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classify", methods=['POST'])
def classify():
    img = request.files['file_key']
    return "Classify"
