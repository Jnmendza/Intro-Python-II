from room import Room
from player import Player
from item import Item

# Declare all the items
item = [
     Item('torch', "Light it up"), #0
     Item('sword',"Shank"), #1
     Item('shield',"Get these haters off you"), #2
     Item('blow-dart', "Poison darts to the neck should work"), #3
     Item('potion', "Drink this and ....vaya con dios amigo!"), #4
     Item('armor', "Bullet proof!"), #5
     Item('A cold one', "Enjoy!!") #6
]

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [item[0]]
                    ),

    'foyer': Room("at the Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                  [item[2]]
                  ),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [item[3]]
                     ),

    'narrow': Room("at the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                   [item[1],
                    item[5]]
                   ),

    'treasure': Room("at the Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [item[4],
                      item[6]]
                     ),
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

p = Player(input("Type players name: "), room['outside'], item[0])
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
                 f'w or q to Quit! You are holding a {p.inventory})\nDirection: ')

    if move in ['n', 'e', 's', 'w']:
        new_room = getattr(p.current_room, f'{move}_to')
        if new_room is None:
            print("cannot go that way")
        else:
            p.current_room = new_room
    else:
        print("invalid command")


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.