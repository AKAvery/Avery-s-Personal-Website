from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    css_url = url_for('static', filename='css/index.css')
    print(css_url)
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(port = 4000, debug=True)