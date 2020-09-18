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
    return render_template('world.html', title=worldTitle, worldContent=worldContent, showEvents=helper.checkBox(boxes[0], 2), showStory=helper.checkBox(boxes[0], 1))

@app.route('/world/<worldTitle>/worldId=<worldId>/worldEvent/eventId=<eventId>')
def world_event(worldTitle, worldId, eventId):
    event = db.getEvent(eventId)
    print(event[0])
    worldContent = helper.getWorldContent(worldId)
    #TODO: get event boxes
    return render_template('event.html', title=event[0][1], worldContent=worldContent, event=event[0])