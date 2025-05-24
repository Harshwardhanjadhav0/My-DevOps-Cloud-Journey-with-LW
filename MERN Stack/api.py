from flask import Flask, request, render_template_string

app = Flask(__name__)
	
@app.route("/search")
def mysearch():
	return "I've done searching"

@app.route("/mail")
def mymail():
	return "email sent successfully"

app.run()