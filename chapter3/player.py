playerDict = {}
saveFile = False
exitSystem = False
# Enter a loop to enter inforation from keyboard
while not exitSystem:
    print 'Sports Team Administration App'
    enterPlayer = raw_input("Would you like to create a team or manage an existing team?\n (Enter 'C' for create, 'M' for manage, 'X' to exit) ")
    if enterPlayer.upper() == 'C':
        exitSystem = False
    # Enter a player for the team
        print 'Enter a list of players on our team along with their position'
        enterCont = 'Y'
        #  While continuing to enter new players, perform the following
        while enterCont.upper() == 'Y':
            name = raw_input('Enter players first name: ')
            position = raw_input('Enter players position: ')
            playerDict[name] = position
            saveFile = True
            enterCont = raw_input("Enter another player? (Press 'N' to exit or 'Y' to continue)")
        else:
            exitSystem = True
    elif enterPlayer.upper() == 'M':
        exitSystem = False
        # Read values from the external file into a dictionary object
        print '\n'
        print 'Manage the Team'
        playerfile = open('players.txt','r')
        for player in playerfile:
            playerList = player.split(':')
            playerDict[playerList[0]] = playerList[1]
        print 'Team Listing'
        print '++++++++++++'
        for i, player in enumerate(playerDict):
            print 'Player %s Name: %s -- Position: %s' %(i, player, playerDict[player])
    else:
        exitSystem = True
else:
    # Save the external file and close resources
    if saveFile:
        print 'Saving Team Data...'
        playerfile = open('players.txt','w')
        for player in playerDict:
            playerfile.write(player + ':' + playerDict[player] + '\n')
        playerfile.close()
