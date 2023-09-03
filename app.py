from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


# Replace with your MySQL database credentials
db_host = "localhost"
db_user = "root"
db_password = "Jagadeeshgouda"
db_name = "google_form"
# Function to establish a database connection
def create_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    
@app.route("/", methods=["GET", "POST"])
def span_page():
    if request.method == "POST":
        
      
      

        # Get form data
       email = request.form["email"]
       name = request.form["name"]
       age = request.form["age"]
       qualification = request.form["qualification"]
       education = request.form["education"]
       study = request.form["study"]
       experiance = request.form["experiance"]
       canada1 = request.form["canada1"]
       canada2 = request.form["canada2"]
       country = request.form["country"]
       goals = request.form["goals"]
       english_listn = request.form["english_listn"]
       english_read = request.form["english_read"]
       english_speak = request.form["english_speak"]
       english_write = request.form["english_write"]
       fees_yn = request.form["fees_yn"]
       fees = request.form["fees"]
       gic_yn = request.form["gic_yn"]
       gic = request.form["gic"]
    # Insert form data into the database
       connection = create_connection()
       cursor = connection.cursor()
       sql = "INSERT INTO data ( email, name, age , qualification , education , study , experiance , canada1 , canada2 , country , goals , english_listn , english_read , english_speak , english_write , fees_yn ,fees , gic_yn , gic  ) VALUES ( %s , %s, %s, %s, %s , %s , %s, %s, %s, %s , %s , %s, %s, %s, %s , %s, %s, %s, %s)"
       values = (email, name, age , qualification , education , study , experiance , canada1 , canada2 , country , goals , english_listn , english_read , english_speak , english_write , fees_yn ,fees , gic_yn , gic )
       cursor.execute(sql, values)
       connection.commit()
      
       return "hello "+(name) +"  WELCOME TO EFFIZIENT <br> <br>" + (name) +" your data is successfully sent to your "+(email) + " <br> <br> THANK YOU"
    return render_template("index.html")






if __name__ == "__main__":
    app.run(debug=True)