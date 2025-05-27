#lab02.py

def cyclestep():
    roomText = "Sie befinden sich im Raum"
    directionText = "Ihr Blick ist gerichtet nach"
    actionText = "Ihr Befehl (L-Links, R-Rechts, G-Gehen, X-Ende): "
    print(roomText, str(rooms[roomID]))
    print(directionText, str(directions[directionID]))
    return input(actionText)

welcomeText = """---------------------------------
------------LABYRINTH------------
---------------------------------"""
closureText = """---------------------------------
-------------Bye Bye-------------
---------------------------------
"""
wrongInputText = "Falsche Eingabe. Versuche nochmal."

roomID = 0
directionID = 0
rooms = ["Kuche", "Wohnzimmer", "Bad"]
directions = ["Norden", "Osten", "Suden", "Westen"]
connections = [["Kuche", "Norden"], ["Wohnzimmer", "Suden"], ["Wohnzimmer", "Osten"], ["Bad", "Westen"]]

print(welcomeText)

while True:
    userInput = cyclestep()
    if userInput == "L" or userInput == "l":
        if directionID == 0:
            directionID = len(directions) - 1
        else:
            directionID -= 1
    elif userInput == "R" or userInput == "r":
        if directionID == len(directions) - 1:
            directionID = 0
        else:
            directionID += 1
    elif userInput == "G" or userInput == "g":
        placement = [rooms[roomID], directions[directionID]]
        if placement in connections:
            if placement[0] == rooms[0]:
                roomID = 1
            elif placement[0] == rooms[1] and placement[1] == directions[2]:
                roomID = 0
            elif placement[0] == rooms[1] and placement[1] == directions[1]:
                roomID = 2
            elif placement[0] == rooms[2]:
                roomID = 1
        else:
            print("Geht nicht")
    elif userInput == "X" or userInput == "x":
        break
    else:
        print(wrongInputText)

print(closureText)



