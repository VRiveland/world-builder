from app import cur, mydtb

def executeWithVariables(query, variables):
    cur.execute(query, variables)
    rows = cur.fetchall()
    return rows

def executeWithoutVariables(query):
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def getWorlds():
    query = "SELECT * FROM Worlds"
    return executeWithoutVariables(query)

def getWorld(worldId):
    query = ("SELECT * FROM Worlds WHERE world_id=%s")
    return executeWithVariables(query, worldId)

def getWorldEvents(worldId):
    query = ("SELECT * FROM Events WHERE world_id=%s AND event_type='world'")
    return executeWithVariables(query, worldId)

def getWorldBoxes(worldId):
    query = ("SELECT * FROM WorldBoxes WHERE world_id=%s")
    return executeWithVariables(query, worldId)

def getEvent(eventId):
    query = ("SELECT * FROM Events WHERE event_id=%s")
    return executeWithVariables(query, eventId)