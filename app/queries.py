from app import cur, mydtb

def getWorlds():
    cur.execute("SELECT * FROM Worlds")
    worlds = cur.fetchall()
    return worlds
    