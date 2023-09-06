from flask import Flask, render_template
import psycopg2
from psycopg2.extensions import parse_dsn
import os

app = Flask(__name__)
con = psycopg2.connect(**parse_dsn(os.environ["POSTGRES_URL"]))

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/insert')
def insert():
	cur = con.cursor()
	cur.execute("INSERT INTO users VALUES ('Bob', '123')")
	con.commit()
	return 'INSERT'

@app.route('/select')
def select():
	cur = con.cursor()
	cur.execute("SELECT * FROM users")
	rows = cur.fetchall()
	return str(rows)
