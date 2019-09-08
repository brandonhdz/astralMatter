from flask import Flask
from flask import render_template, request
from dataParser import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def visualizer():
    return render_template('about.html')

@app.route('/artwork')
def openloop():
    return render_template('artwork.html')

@app.route('/music')
def ai_text_generator():
    return render_template('music.html')