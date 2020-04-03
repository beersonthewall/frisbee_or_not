from flask import Flask, render_template, request, flash
from fastai.vision import *

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
MODEL_PATH = 'model/'

app = Flask(__name__)
learner = load_learner(MODEL_PATH)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/classify", methods=['POST'])
def classify():
    if 'file' not in request.files:
        return render_template("index.html", error="No file part")

    file = request.files['file']
    if file.filename == '':
        return render_template("index.html", error="No selected file part")

    if file and allowed_file(file.filename):
        bytes = file.read()
        img = open_image(BytesIO(bytes))
        prediction,_,outputs = learner.predict(img)
        return render_template("index.html", prediction=prediction, losses=outputs)
    else:
        flash('File type not allowed')
        return redirect(request.url)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
