from flask import Flask, render_template
import os
import psycopg2

app = Flask(__name__)
POSTGRES_URL = os.environ['POSTGRES_URL']

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/create')
def create():
	try:
		con = psycopg2.connect(POSTGRES_URL, sslmode='require')
		cur = con.cursor()
		cur.execute(	"""	CREATE TABLE Users(
						Username VARCHAR(20) NOT NULL PRIMARY KEY,
						Password VARCHAR(20) NOT NULL
							  )
				""")
		con.commit()
		return 'CREATE'
	except Exception as e:
		return str(e)

@app.route('/insert')
def insert():
	try:
		con = psycopg2.connect(POSTGRES_URL, sslmode='require')
		cur = con.cursor()
		cur.execute("INSERT INTO users VALUES ('Bob', '123')")
		con.commit()
		return 'INSERT'
	except Exception as e:
		return str(e)

@app.route('/select')
def select():
	try:
		con = psycopg2.connect(POSTGRES_URL, sslmode='require')
		cur = con.cursor()
		cur.execute("SELECT * FROM users")
		rows = cur.fetchall()
		con.close()
		return str(rows)
	except Exception as e:
		return str(e)
