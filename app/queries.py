from app import cur, mydtb

#Execution
def executeWithVariables(query, variables):
    cur.execute(query, variables)
    rows = cur.fetchall()
    return rows

def executeWithoutVariables(query):
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def executeWithoutReturn(query, variables):
    cur.execute(query, variables)
    mydtb.commit()

#Queries
def getWorlds():
    query = "SELECT * FROM Worlds"
    return executeWithoutVariables(query)

def getWorld(worldId):
    query = ("SELECT * FROM Worlds WHERE world_id = %s")
    world = executeWithVariables(query, worldId)
    return world[0]

def addWorld(worldTitle, description, story):
    query = ("INSERT INTO Worlds (title, descr, story) Values (%s, %s, %s)")
    executeWithoutReturn(query, [worldTitle, description, story])

#Info contains (worldTitle, description, story, WorldId)
def updateWorld(info):
    query = ("UPDATE Worlds SET title=%s, descr=%s, story=%s WHERE world_id=%s")
    executeWithoutReturn(query, info)

def getNewWorldId():
    query = "SELECT LAST_INSERT_ID() FROM Worlds"
    temp = executeWithoutVariables(query)
    return temp[0][0]

def getWorldEvents(worldId):
    query = ("SELECT * FROM Events WHERE world_id=%s AND event_type='world'")
    return executeWithVariables(query, worldId)

def getEvent(eventId):
    query = ("SELECT * FROM Events WHERE event_id=%s")
    return executeWithVariables(query, eventId)