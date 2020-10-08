import app.queries as db

def getWorldContent(worldId):
    world = db.getWorld(worldId)
    events = db.getWorldEvents(worldId)
    if events == []:
        events = None
    return world, events