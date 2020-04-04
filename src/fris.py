from flask import Flask, render_template, request, flash
from fastai.vision import open_image, Learner, load_learner
from io import BytesIO

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
MODEL_PATH = 'model/'
INDEX_TEMPLATE = "index.html"

app = Flask(__name__)
learner = load_learner(MODEL_PATH)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/classify", methods=['POST'])
def classify():
    if 'file' not in request.files:
        return render_template(INDEX_TEMPLATE, error="No file part.")

    file = request.files['file']
    if file.filename == '':
        return render_template(INDEX_TEMPLATE, error="No selected file part.")

    if file and allowed_file(file.filename):
        bytes = file.read()
        img = open_image(BytesIO(bytes))
        prediction,label,outputs = learner.predict(img)
        return render_template(INDEX_TEMPLATE, prediction=prediction, confidence=outputs[label])
    else:
        return render_template(INDEX_TEMPLATE, error="File type not allowed.")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
