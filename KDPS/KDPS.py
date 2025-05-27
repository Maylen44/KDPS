#lab04.py

def cyclestep():
    roomText = "Sie befinden sich im Raum"
    directionText = "Ihr Blick ist gerichtet nach"
    actionText = "Ihr Befehl (L-Links, R-Rechts, G-Gehen, X-Ende): "
    print(roomText, roomID)
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

roomID = 'Kuche'
directionID = 0
directions = ["Norden", "Osten", "Suden", "Westen"]
connections = {
    ('Kuche', 0) : 'Wohnzimmer',
    ('Wohnzimmer', 2) : 'Kuche',
    ('Wohnzimmer', 3) : 'Bad',
    ('Bad', 1) : 'Wohnzimmer' }

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
        placement = (roomID, directionID)
        if placement in connections:
            roomID = connections[placement]            
        else:
            print("Geht nicht")
    elif userInput == "X" or userInput == "x":
        break
    else:
        print(wrongInputText)

print(closureText)



