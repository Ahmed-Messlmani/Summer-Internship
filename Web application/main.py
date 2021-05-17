from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
import pickle
import pandas as pd 
import numpy as np 
from matplotlib import pyplot
import flask
from flask import Flask,render_template,url_for,request,flash,jsonify,Response

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/acceuil')
@login_required
def home():
	return render_template('Home.html')
	
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)



@main.route('/predictindex', methods=['POST'])
def predictindex():

	cleandata=open('C:/Users/ahmed/OneDrive/Bureau/login/project/models/testword.txt',encoding='latin-1').read().splitlines()
	while '' in cleandata:
		cleandata.remove('')
	
	# Receives the input query from form
	if request.method == 'POST':

		element = request.form['mydata']
		text = [element]
		if(request.form['predict'] == 'Predict'):
			trouve=False
			for s in cleandata:
				if s in element:
					trouve=True
					break
			if(trouve==True):
				x=0
			else:
				f = open('C:/Users/ahmed/OneDrive/Bureau/login/project/models/naivebayesfinal1.pickle', 'rb')
				classifier = pickle.load(f)
				x=classifier.predict(text)
		
	return render_template('result.html',prediction = x)