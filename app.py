from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)


host=os.environ["POSTGRES_HOST"]
database=os.environ["POSTGRES_DATABASE"]
user=os.environ["POSTGRES_USER"]
password=os.environ["POSTGRES_PASSWORD"])
con = psycopg2.connect()

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/create')
def create():
	cur = con.cursor()
	cur.execute(	"""	CREATE TABLE users(
				Username VARCHAR(20) NOT NULL PRIMARY KEY,
				Password VARCHAR(20) NOT NULL
					)
			""")
	con.commit()
	return 'CREATE'

@app.route('/insert')
def insert():
	cur = con.cursor()
	cur.execute("INSERT INTO users VALUES ('Bob', '123')")
	con.commit()
	con.close()
	return 'INSERT'

@app.route('/select')
def select():
	cur = con.cursor()
	cur.execute("SELECT * FROM users")
	rows = cur.fetchall()
	return str(rows)

@app.route('/rollback')
def rollback():
	con.rollback()
	return 'rollback'
