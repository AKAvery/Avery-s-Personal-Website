from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(__name__, static_folder="../static", template_folder="../templates")

# Home
@app.get("/")
def home():
    return render_template("index.html")

# Explicit simple pages
@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/projects")
def projects():
    return render_template("projects.html")

@app.route('/fistbump')
def fistbump():
    return render_template('IndividualProjects/fistbump.html')

@app.route('/stockSentiment')
def stockSentiment():
    return render_template('IndividualProjects/stockSentiment.html')

@app.route('/andersonCodingClub')
def andersonCodingClub():
    return render_template('IndividualProjects/andersonCodingClub.html')

@app.route('/kneeEd')
def kneeEd():
    return render_template('IndividualProjects/KneeEd.html')

@app.route('/canKiosk')
def canKiosk():
    return render_template('IndividualProjects/canKiosk.html')

# Generic fallback: serve any template by path
# Supports /page  -> templates/page.html
#         /foo/bar -> templates/foo/bar.html
@app.get("/<path:page>")
def serve_page(page):
    for name in (page, f"{page}.html"):
        try:
            return render_template(name)
        except TemplateNotFound:
            pass
    abort(404)
