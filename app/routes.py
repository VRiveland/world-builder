from flask import render_template, redirect, url_for
from app import app
import app.helpers as helper
import app.queries as db
import app.forms as forms

@app.route('/')
@app.route('/index')
def index():
    worlds = db.getWorlds()
    return render_template('index.html', title='Worlds', worlds=worlds)

@app.route('/world/<worldTitle>/worldId=<worldId>')
def world(worldTitle, worldId):
    worldContent = helper.getWorldContent(worldId)
    return render_template('world.html', title=worldTitle, worldContent=worldContent)

@app.route('/add_world', methods=['GET', 'POST'])
def add_world():
    form = forms.WorldForm()
    if form.validate_on_submit():
        info = [form.title.data]
        if form.descr.data:
            info.append(form.descr.data)
        else:
            info.append("Not yet added")
        if form.story.data:
            info.append(form.story.data)
        else:
            info.append("Not yet added")
        db.addWorld(info[0], info[1], info[2])
        this = db.getNewWorldId()
        return redirect(url_for("world", worldTitle=info[0], worldId=this))
    return render_template('addWorld.html', title="Add New World", form=form)

@app.route('/edit_world/<worldTitle>/worldId=<worldId>', methods=['GET', 'POST'])
def edit_world(worldTitle, worldId):
    title = "Edit " + worldTitle
    form = forms.WorldForm()
    if form.validate_on_submit():
        info = [form.title.data]
        if form.descr.data:
            info.append(form.descr.data)
        else:
            info.append("Not yet added")
        if form.story.data:
            info.append(form.story.data)
        else:
            info.append("Not yet added")
        info.append(worldId)
        db.updateWorld(info)
        return redirect(url_for("world", worldTitle=info[0], worldId=worldId))
    this = db.getWorld(worldId)
    form.title.data = worldTitle
    form.descr.data = this[2]
    form.story.data = this[3]
    return render_template('addWorld.html', title=title, form=form)

@app.route('/world/<worldTitle>/worldId=<worldId>/worldEvent/eventId=<eventId>')
def world_event(worldTitle, worldId, eventId):
    event = db.getEvent(eventId)
    worldContent = helper.getWorldContent(worldId)
    return render_template('event.html', title=event[0][1], worldContent=worldContent, event=event[0])