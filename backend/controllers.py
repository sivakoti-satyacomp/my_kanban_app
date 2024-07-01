
from flask import Flask,render_template,request
from flask import current_app as app #Alias for current running app
from .models import *

@app.route("/") #it refers base url 127.0.0.1:5000
def home():
    return "<h2>Welcome to Kanban app</h2>"

@app.route("/register",methods=["GET","POST"]) #it refers base url+/signup
def user_signup():
    if request.method=="POST":
        email=request.form.get("email")
        full_name=request.form.get("full_name")
        uname=request.form.get("uname")
        pwd=request.form.get("pwd")
        usr=User_Info.query.filter_by(user_name=uname).first() #Get existig user matched
        if not usr:
            new_user=User_Info(email=email,full_name=full_name,user_name=uname,pwd=pwd)
            db.session.add(new_user)
            db.session.commit()
            return render_template("login.html",msg="")
        else:
            return render_template("signup.html",msg="Sorry, User is already existed!!")
    
    return render_template("signup.html",msg="")


@app.route("/login",methods=["GET","POST"]) #it refers base url+/login
def user_login():
    if request.method=="POST":
        uname=request.form.get("uname")
        pwd=request.form.get("pwd")
        usr=User_Info.query.filter_by(user_name=uname, pwd=pwd).first() #Get existig user matched
        if usr and usr.role==0:
            #Add a code read existing user summary from user list
            return render_template("admin_dashboard.html",name=usr.user_name)
        elif usr and usr.role==1:
            return render_template("user_dashboard.html",name=usr.user_name)
        else:
            return render_template("login.html",msg="Invalid credentials!!")
    
    return render_template("login.html",msg="")

#more routes here
#lot of routes
