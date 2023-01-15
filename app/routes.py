from flask import render_template
from app import app
from app.scripts import getCatalog

@app.route('/')
def home():
    catalog = getCatalog()
    return render_template('home.html', catalog = catalog);