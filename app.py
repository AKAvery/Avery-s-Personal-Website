from flask import Flask, render_template, url_for

app = Flask(__name__)

# Endpoint names must match api/index.py, because the templates call
# url_for('knee_ed'), url_for('stock_sentiment'), etc.

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
    return render_template('IndividualProjects/fistbump.html')

@app.route('/stockSentiment')
def stock_sentiment():
    return render_template('IndividualProjects/stockSentiment.html')

@app.route('/andersonCodingClub')
def anderson_coding_club():
    return render_template('IndividualProjects/andersonCodingClub.html')

@app.route('/kneeEd')
def knee_ed():
    return render_template('IndividualProjects/kneeEd.html')

@app.route('/canKiosk')
def can_kiosk():
    return render_template('IndividualProjects/canKiosk.html')

@app.route('/kalshiBot')
def kalshi_bot():
    return render_template('IndividualProjects/kalshiBot.html')

@app.route('/cossmology')
def cossmology():
    return render_template('IndividualProjects/cossmology.html')

@app.route('/premedCopilot')
def premed_copilot():
    return render_template('IndividualProjects/premedCopilot.html')

@app.route('/longhornNeurotech')
def longhorn_neurotech():
    return render_template('IndividualProjects/longhornNeurotech.html')

@app.route('/orcaStrike')
def orca_strike():
    return render_template('IndividualProjects/orcaStrike.html')

if __name__ == '__main__':
    app.run(port=4000, debug=True)
