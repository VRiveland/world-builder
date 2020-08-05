from flask import render_template
from app import app
import app.queries as db

@app.route('/')
@app.route('/index')
def index():
    #TODO: get world info from db
    worlds = db.getWorlds()
    return render_template('index.html', title='Worlds', worlds=worlds)