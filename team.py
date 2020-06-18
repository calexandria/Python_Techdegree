# TODO Create an empty list to maintain the player names

players = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'

add_players = input("Would you like to add a player to the list?\n Yes or No   ")

while add_players.lower() == 'yes':
    name = input("\nEnter the name of the player you'd like to add: ")
    players.append(name)
    add_players = input("Would you like to add another player? \n Yes or No  ")


# TODO print the number of players on the team
  
print("\nWe have {} players on the team.".format(len(players)))

# TODO Print the player number and the player name
# The player number should start at the number one

player_number = 1
for player in players:
    print("Player {}: {}".format(player_number,name))
    player_number += 1

# TODO Select a goalkeeper from the above roster

keeper = input("Please select the goal keeper by selecting the player number. (1-{})".format(len(players)))
               
keeper = int(keeper)

# TODO Print the goal keeper's name

print("Great!!! The goalkeeper selected is {}".format(players[keeper - 1]))
# Remember that lists use a zero based index

