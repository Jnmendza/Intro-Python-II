from room import Room
from player import Player
import sys
# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),
    'foyer': Room("at the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow': Room("at the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("at the Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#
# Main
#
# Make a new player object that is currently in the 'outside' room.

p = Player(input("Type players name: "), room['outside'])
# print(p)

play = input('Would you like to play a game? (y/n): ')
if play == "y":
    print('great!')
elif play == "n":
    print('too bad!')
else:
    print('invalid answer')

# Write a loop that:
while play == "y":
    move = input(f'{p.name}, you are currently {p.current_room}\nWhere would you like to go? (n, s, e, '
                 f'w or q to Quit!)\nDirection: ')

    if move == "n":
        if p.current_room.n_to is None:
            print("you cannot go that way from here")
        else:
            p.current_room = p.current_room.n_to

    elif move == "e":
        if p.current_room.e_to is None:
            print("you cannot go that way from here")
        else:
            p.current_room = p.current_room.e_to

    elif move == "s":
        if p.current_room.s_to is None:
            print("you cannot go that way from here")
        else:
            p.current_room = p.current_room.s_to

    elif move == "w":
        if p.current_room.w_to is None:
            print("you cannot go that way from here")
        else:
            p.current_room = p.current_room.w_to

    elif move == "q":
        print("See you next time!")
        sys.exit()

    else:
        print("That is not a valid command. Try Again!")

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.