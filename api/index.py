from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

# api/index.py lives under /api, so go up one level for templates/static
app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/projects")
def projects():
    return render_template("projects.html")

# Individual project pages (match your template filenames exactly, case-sensitive!)
@app.get("/kneeEd")
def knee_ed():
    return render_template("IndividualProjects/kneeEd.html")

@app.get("/fistbump")
def fistbump():
    return render_template("IndividualProjects/fistbump.html")

@app.get("/andersonCodingClub")
def anderson_coding_club():
    return render_template("IndividualProjects/andersonCodingClub.html")

@app.get("/canKiosk")
def can_kiosk():
    return render_template("IndividualProjects/canKiosk.html")

@app.get("/stockSentiment")
def stock_sentiment():
    return render_template("IndividualProjects/stockSentiment.html")

# Optional generic fallback: /foo -> templates/foo.html, /foo/bar -> templates/foo/bar.html
@app.get("/<path:page>")
def serve_page(page):
    for name in (page, f"{page}.html"):
        try:
            return render_template(name)
        except TemplateNotFound:
            pass
    abort(404)

# No app.run() here; Vercel imports `app`
