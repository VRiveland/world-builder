from flask import render_template
from app import app
import app.helpers as helper
import app.queries as db

@app.route('/')
@app.route('/index')
def index():
    #TODO: get world info from db
    worlds = db.getWorlds()
    return render_template('index.html', title='Worlds', worlds=worlds)

@app.route('/world/<worldTitle>/worldId=<worldId>')
def world(worldTitle, worldId):
    worldContent = helper.getWorldContent(worldId)
    boxes = db.getWorldBoxes(worldId)
    return render_template('world.html', title=worldTitle, world=worldContent[0], worldEvents=worldContent[1], showEvents=helper.checkBox(boxes[0], 2), showStory=helper.checkBox(boxes[0], 1))