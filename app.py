from flask import Flask, render_template, request, redirect, url_for
import time as t
app = Flask(__name__)
@app.route("/")
def home():
  return render_template("login.css.html")
@app.route("/login", methods=["POST"])
def login():
  name = request.form.get("username")
  #t.sleep(3)
  return render_template( "logged.html", name = name)
app.run(debug=True) 