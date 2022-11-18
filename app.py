from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
# from flask import login_required
import os
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash 
from cs50 import SQL

# Flask login managerhttps://flask-login.readthedocs.io/en/latest/
# login_manager = LoginManager()

# Configuration application adapted from CS50 final project, CS50x PSET 9 and Stackoverflow https://stackoverflow.com/questions/31002890/how-to-reference-a-html-template-from-a-different-directory-in-python-flask)
app = Flask(__name__, template_folder="./templates")
# login_manager.init_app(app)

# Ensure templates are auto-reloaded(from CS50 PSET 9)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configure session to use filesystem (instead of cookies) from CS50 PSET 9
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Handle cache (from CS50 PSET 9)
@app.after_request
def after_request(response):
  """Ensure responses aren't cached"""
  response.headers["Cache-control"] = "no-cache, no-store, must-revalidate"
  response.headers["Expires"] = 0
  response.headers["Pragma"] = "no-cache"
  return response

# About page
@app.route("/about")
def about():
  """About page explaining why this was made"""
  return render_template("about.html")

@app.route("/contact")
def contact():
  """Contact page in case anyone has questions"""
  return render_template("contact.html")

@app.route("/")
def home():
  """Home page brief explanation"""
  return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  """Admin wants to login"""
  #Forgets user_id
  session.clear()
  if request.method == "POST":
    username = request.form.get("email")
    password = request.form.get("password")

    if username == "TokiLoshiCodes" and password == "rumbat":
      print("Valid username and password")
      redirect("/news")
    else:
      flash("Something went wrong")
      return  render_template("/login.html")
  else:
    return render_template("/login.html")

# News page
@app.route("/news", methods=["GET", "POST"])
# @login_required
def news():
  """Show Admin the news"""
  if request.method == "POST":
    flash("News Time")
    print("Time to get the news")
    return render_template("news.html")
  else:
    flash("Get request, and we can get the news")
    print("Time to get the news")
    return render_template("news.html")