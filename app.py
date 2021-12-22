# import flask
from flask import Flask
# Create an app, being sure to pass_Name_
app = Flask(__name__)
# define what to do when a user gets to the index route
@app.route('/')
def home():
    print("Server received request for 'Home' page ...")
    return "Welcome to my 'Home' page!"

# Define what to do when a user goes to the / about route
@app.route("/about")
def about():
    print("Server received requests for 'About' page ...")
    return "Welcome to my 'About' page!"
if __name__ == "__main__":
    app.run(dubug=True)
