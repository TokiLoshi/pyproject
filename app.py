from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from helpers import login_required
from werkzeug.security import check_password_hash, generate_password_hash
import os
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash 
from cs50 import SQL
import os
from project import main, get_date_time

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

# Configure CS50 Library to use SQLite and adapt to tranfer to PostGres for Heroku deployment
# https://cs50.readthedocs.io/heroku/
# uri = os.getenv("DATABASE_URL")
# if uri.startswith("postgres:"):
#   uri = uri.replace("postgress://", "postgresql://")

# db = SQL("sqlite:///news.db")

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://")
db = SQL(uri)

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
    print("Username: ", username)
    print("Password: ", password)

    if username == "silvabee@gmail.com" and password == "wombat":
      print("Valid username and password")
      session["user_id"] = 1
      return redirect("/news")
    elif username == "visitor@notarealemail.com" and password == "curiouser":
      session["user_id"] = 2
      return redirect("/news")
    else:
      flash("Something went wrong")
      return  render_template("/login.html")
  else:
    return render_template("/login.html")

# News page
@app.route("/news", methods=["GET", "POST"])
@login_required
def news():
  """Show Admin the news"""
  if request.method == "POST":
    flash("News Time")
    return redirect("/news")
  else:
    flash("News Time")
    tech_news, sf_news, africa_news, sa_news = main()
    current_sf, current_eastcoast, current_time_europe, current_time_africa = get_date_time()
    print(current_sf)
    print(current_eastcoast)
    print(current_time_europe)
    print(current_time_africa)

    return render_template("news.html", africatime=current_time_africa, zurichtime=current_time_europe, nytime=current_eastcoast, sftime=current_sf, tech_news=tech_news, sf_news=sf_news, africa_news=africa_news, sa_news=sa_news)

# Log out
@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
  """Log out"""
  session.clear()
  return render_template("/login.html")