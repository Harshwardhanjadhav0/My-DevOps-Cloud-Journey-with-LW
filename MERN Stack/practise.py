from flask import Flask, request, render_template_string

app = Flask(__name__)
html_template= """
<!DOCTYPE html>
<html>
<head>
	<title> Kya bolra ?</title>
</head>
<body>
	<h1> Submit Your Vishay</h1>
<form action="/submit" method="post">
	<b><lable for ="first name"> First Name: </lable></b> 
	<input type="text" required>
  	<br><br>
	
	<b><lable for ="Surname"> Surname: </lable></b>
	<input type="text" required>
	<br><br>

	<b><lable for ="middle name"> Middle Name: </lable></b>
	<input type="text" required>
	<br><br>

	<b><lable for ="kya kaam ?"> Kya Kaam ?:-</lable></b><br>
	<textarea id="kya kaam ?" name="kya kaam ?"  rows="4" cols="20" required></textarea>
	<br><br>

	<input type="submit" value="Submit">
 	<input type="reset" value="Nako">
</form>
</body>
</html>	
"""
@app.route("/")
def form():
    return render_template_string(html_template)

@app.route("/submit", methods=["POST"])
def submit():
    name=request.form.get("first name")
    surname=request.form.get("surname")
    middle=request.form.get("middle name")
    kaam=request.form.get("kya kaam ?")
    
    filename = f"{name, surname, middle}_vishay.txt"
    with open (filename, "w") as file:
        file.write(f"First Name: {name}")
        file.write(f"Surname: {surname}")
        file.write(f"Middle Name: {middle}")          
        
    return f"Vishay sort successfully ! file{filename} created"
    
app.run()