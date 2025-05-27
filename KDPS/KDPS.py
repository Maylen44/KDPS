#lab05.py

def getNewDirection(direction, turn, numdirections):
    return (direction + turn) % numdirections

def getNewRoom(room, direction, connections):
    if (room, direction) in connections:
        return connections[(room, direction)]
    else:
        return None

print("-" * 33)
print("-" * 12 + "LABYRINTH" + "-" * 12)
print("-" * 33)

directions  = ["Norden", "Osten", "Süden", "Westen"]
connections = {
    ("Küche"     , 0): "Wohnzimmer",
    ("Wohnzimmer", 2): "Küche",
    ("Wohnzimmer", 1): "Bad",
    ("Bad"       , 3): "Wohnzimmer"
}

room      = "Küche"
direction = 0

print(f"Sie befinden sich im Raum '{room}'.")
print(f"Ihr Blick ist nach '{directions[direction]}' gerichtet.")

while True:
    z = input("Ihr Befehl (L-Links, R-Rechts, G-Gehen, X-Ende): ").upper()
    if z == "L":
        direction = getNewDirection(direction, -1, len(directions))
        print(f"Neue Blickrichtung: {directions[direction]}")
    elif z == "R":
        direction = getNewDirection(direction, +1, len(directions))
        print(f"Neue Blickrichtung: {directions[direction]}")
    elif z == "G":
        newRoom = getNewRoom(room, direction, connections)
        if newRoom is not None:
            room = newRoom
            print(f"Neuer Raum: {room}")
        else:
            print("Geht nicht.")
    elif z == "X":
        break
print("Bye.")