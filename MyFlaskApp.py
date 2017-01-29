#import  flask
from flask import Flask
from flask import render_template
from flask import request

app = Flask (__name__)

# create URL & function mapping for root or /
@app.route("/")
def index():
    return "hello from Flask!!!"

# create another mapping for /hello
@app.route("/hello")
def hello():
    myName ="Ryan"
    return "hello again !!" + myName

#create mapping for /myprofile
@app.route("/myprofile")
def showmyprofile():
    return render_template("MyProfileForm.html")

# create a mapping for /addprofile
@app.route("/addprofile")
def addprofile():
    myname = request.args.get("myname")
    state_of_residence = request.args.get("state_of_residence")
    return render_template("MyProfile.html",myname=myname,state_of_residence=state_of_residence)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000")

