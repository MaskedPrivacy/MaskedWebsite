"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, send_from_directory
from PrivacyWebsite import app

@app.before_request
def before_request():

    if request.is_secure:
        return

    url = request.url.replace("http://", "https://", 1)
    code = 301
    return redirect(url, code=code)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    """Renders the home page."""
    return render_template('index.html', title='Masked Privacy')


@app.route('/documentation/', methods=['GET'])
def Documentation():
        return render_template('documentation.html')

@app.route('/obfuscator/', methods=['GET', 'POST'])
def Obfuscator():
    """Renders the about page."""
    return render_template( 'obfuscator.html')

@app.route('/legal/', methods=['GET'])
def Legal():
    return render_template('legal.html')

@app.route('/staking/', methods=['GET'])
def Staking():
    return render_template('staking.html')

@app.route('/circulating/', methods=['GET'])
def Circulating():
    return '81052 MASKED' #todo, grab from some spot where we can store this value, maybe a db

@app.route('/circulating/raw/', methods=['GET'])
def RawCirculating():
    return '81052000000000000000000 MASKED'

@app.route('/test/', methods=['GET'])
def test():
    return render_template('test.html')

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
