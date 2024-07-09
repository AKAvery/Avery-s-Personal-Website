from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/fistbump')
def fistbump():
    return render_template('individualProjects/fistbump.html')

@app.route('/stockSentiment')
def stockSentiment():
    return render_template('individualProjects/stockSentiment.html')

if __name__ == '__main__':
    app.run(port = 4000, debug=True)