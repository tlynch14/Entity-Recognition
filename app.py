from flask import Flask, render_template, request
import spacy
from spacy import displacy
from ner_client import NamedEntityClient

app = Flask(__name__)

ner = spacy.load("en_core_web_sm")
ner = NamedEntityClient(ner, displacy)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
