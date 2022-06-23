
from flask import Flask, render_template, request, flash, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)
messages = list()
####### Generating Secret Key
key = os.urandom(12).hex()
app.config['SECRET_KEY'] = str(key)

@app.route("/")
def home():
  return render_template("index.html", messages = messages)

@app.route("/save", methods=["POST"])
def save():
  vid = request.form.get('link')
  video = YouTube(vid)
  if request.form.get('download') or vid != '':
    messages.append('Downloading')
    for i in messages:
      print(i)
  stream = video.streams.get_highest_resolution()
  stream.download()
  print("downloading")
  return redirect(url_for("home"))


#<a href="/images/myw3schoolsimage.jpg" download></a>