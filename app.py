from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

conn_dict =  psycopg2.conninfo.conninfo_to_dict(os.environ["POSTGRES_URL"])

#con = psycopg2.connect(
#host=os.environ["POSTGRES_HOST"],
#database=os.environ["POSTGRES_DATABASE"],
#user=os.environ["POSTGRES_USER"],
#password=os.environ["POSTGRES_PASSWORD"])

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/create')
def create():
	con = psycopg2.connect(**conn_dict)
	cur = con.cursor()
	cur.execute(	"""	CREATE TABLE users(
				Username VARCHAR(20) NOT NULL PRIMARY KEY,
				Password VARCHAR(20) NOT NULL
					);
			""")
	con.commit()
	return 'CREATE'

@app.route('/tables')
def tables():
	cur = con.cursor()
	cur.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
	rows = cur.fetchall()
	return str(rows)

@app.route('/insert')
def insert():
	cur = con.cursor()
	cur.execute(	"""	INSERT INTO users (Username, Password)
					VALUES ("Bob", "123");
			""")
	con.commit()
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
