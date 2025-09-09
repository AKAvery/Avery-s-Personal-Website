from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.get("/")
def home():
    return render_template("index.html")     # your existing template

# if your pages link to /static/*
@app.get("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)
