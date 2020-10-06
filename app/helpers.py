import app.queries as db

def getWorldContent(worldId):
    world = db.getWorld(worldId)
    events = db.getWorldEvents(worldId)
    if events == []:
        events = None
    return world, events

def checkBox(boxes, place):
    show = False
    if boxes[place] == 1:
        show = True
    return show