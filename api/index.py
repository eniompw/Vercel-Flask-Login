from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('login.html')
	
@app.route('/debug')
def debug():
	url = os.environ["POSTGRES_URL"]
	return url
