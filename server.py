from flask import Flask
from flask import render_template
from flask import request

import numpy as np
from scipy import stats
from random import randint

from time import strftime

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import model

# create a flask application
app = Flask(__name__)

# "@" prefix tells us we're dealing with decorater
# python decorator that will act on the function definition that follows it.
# app, the flask application can be used to define routes or url within our webserver
@app.route('/') # / > means it's the homepage
def index():
	return render_template('index.html', name='Ada')
    #return 'Hello, World!'

@app.route('/roll_dice')
def roll_dice():
	die = stats.randint(1,7)
	result = die.rvs(3)
	return ("Giving you results from 3 dice rolls: " + str(result))

@app.route('/roll_dice/<int:ndice>') #turn ndice from str into int
def roll_dice_option(ndice):
	rolls = [randint(1,6) for _ in range(1,ndice+1)]
	
	return render_template('roll-dice.html', name='Ada', rolls=rolls)

# @app.route('/roll_dice/<int:ndice>') #turn ndice from str into int
# def roll_dice_option(ndice):
# 	rolls = [randint(1,6) for _ in range(1,6)]
# 	output = "<h3>Here are your dice rolls: </h3>"
# 	output += '<br />'
# 	for roll in rolls:
# 		output += str(roll) + '<br />'
# 	print(output)
# 	return output

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting-result.html', greeting=greeting)


@app.route('/scam_detector')
def scam_detector():
	return render_template('scam_detector.html')

@app.route('/analyze_detector_input', methods=['POST'])
def prediction():
    word = request.form['word']
    result = model.predict(word)

    return render_template('scam_analysis.html', result=result)
	
