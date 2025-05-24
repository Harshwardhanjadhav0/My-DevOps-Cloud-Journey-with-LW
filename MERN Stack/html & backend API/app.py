from flask import Flask, request, render_template_string #importing libraries and frameworks.

app = Flask(__name__) #main function __name__

html_template= """
<!DOCTYPE html>
<html>
<head>
	<title>Course Query Form</title>
</head>
<body>
	<h2>Submit your Query</h2>
	<form action="/submit" method="post">
		<label for="name">Name: </label>
	    	<input type="text" name="name" required> 
 	    	<br><br>

		<label for="email">Email: </label>
	    	<input type="text" name="email" required>
	    	<br><br>

	    	<label for="course">Course: </label>
	    	<input type="text" name="course" required>
	    	<br><br>

	    	<label for="query">Query: </label>
	    	<br>
	    	<textarea id="query" name="query" rows="6" cols="30" required></textarea>
	    	<br>
	    	<input type="submit" value="Submit">
	    	<input type="reset" value="Reset"> 	
	</form>
</body>
</html> 
"""

@app.route("/")
def form():
	return render_template_string(html_template)

@app.route("/submit", methods=["POST"])
def submit():
	#giving varaibles form fiels to its specific varaibles
	name=request.form.get("name")
	email=request.form.get("email")
	course=request.form.get("course")
	query=request.form.get("query")

	filename= f"{name}_query.txt"
	#using "w" for write mode in files.
	with open(filename, "w") as file:
		file.write(f"Name:{name}\n")
		file.write(f"Email:{email}\n")
		file.write(f"Course:{course}\n")
		file.write(f"Query:{query}\n")

	return f"Query Submitted Successfully ! File ({filename}) created"


if __name__ == "__main__":
    app.run() 