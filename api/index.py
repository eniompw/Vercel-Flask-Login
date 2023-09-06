from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('login.html')
	
@app.route('/debug')
def debug():
	conn = psycopg2.connect(
    	host=os.environ["POSTGRES_HOST"],
    	database=os.environ["POSTGRES_DATABASE"],
    	user=os.environ["POSTGRES_USER"],
    	password=os.environ["POSTGRES_PASSWORD"])
	
	cur = con.cursor()
	cur.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
	res = cur.fetchall()
	return str(res)
