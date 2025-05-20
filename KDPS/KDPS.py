#lab02.py

welcomeText = """---------------------------------
------------LABYRINTH------------
---------------------------------"""
actionText = "Ihr Befehl (L-Links, R-Rechts, G-Gehen, X-Ende): "
roomID = 0
directionID = 0
rooms = ["Kuche", "Wohnzimmer", "Schlafzimmer", "Koridor"]
directions = ["Norden", "Osten", "Suden", "Westen"]

print(welcomeText)

while True:
    print("Sie befinden sich in Raum: '%s'." % rooms[roomID])
    print("Ihr Blick ist nach '%s' gerichtet." % directions[directionID])
    playerInput = input(actionText)
    
    if playerInput == 'L' or playerInput == 'l':
        if directionID == 0:
            directionID = 3
        else:
            directionID -= 1
    elif playerInput == 'R' or playerInput == 'r':
        if directionID == 3:
            directionID = 0
        else:
            directionID += 1
    elif playerInput == 'G' or playerInput == 'g':
        match (roomID, directionID):
            case (0, 0):
                roomID = 3
            case (3, 2):
                roomID = 0
            case (3, 1):
                roomID = 1
            case (1, 3):
                roomID = 3
            case (3, 3):
                roomID = 2
            case (2, 1):
                roomID = 3
    elif playerInput == 'X' or playerInput == 'x':
        print("Bye Bye!")
        break
    else:
        print("Falsche Eingabe. Probiere nochmal!")











