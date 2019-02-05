room_list = []
room = ['You made it out!', None, None, None, None]
room_list.append(room)
room = ['You are in the backyard. There are passages to the east and south', None, 2, 4, None]
room_list.append(room)
room = ['You have drowned in the pool. Didn\'t you remember that you don\'t know how to swim? Better luck next time!', None, 3, 5, 1]
room_list.append(room)
room = ['You are in the shallow end of a pool in the backyard. There is a passage to the west.', None, None, None, 2]
room_list.append(room)
room = ['You are in the dining room. There are passages to the north, east, and south.', 1, 5, 8, None]
room_list.append(room)
room = ['You are in the kitchen. There are passages in all directions.', 2, 6, 9, 4]
room_list.append(room)
room = ['You are in the bathroom. There are passages to the south and west.', None, None, 10, 5]
room_list.append(room)
room = ['You are in the kid\'s bathroom. There is a passage to the east', None, 8, None, None]
room_list.append(room)
room = ['You are in the kid\'s bedroom. There are passages to the east, south, and west', None, 9, 11, 7]
room_list.append(room)
room = ['You are in the living room. There are passages in all directions', 5, 10, 12, 8]
room_list.append(room)
room = ['You are in the parent\'s bedroom. There are passages to the north, south, and west.', 6, None, 13, 9]
room_list.append(room)
room = ['You are in the entrance. There are passages to the north, east, and west.', 8, 12, None, 0]
room_list.append(room)
room = ['You are in the hallway. There are passages to the north east and west.', 9, 13, None, 11]
room_list.append(room)
room = ['You are in the garage (it\'s locked). There are passages to the north and west.', 10, None, None,12]
room_list.append(room)

current_room = 9
done = True
turns = 0
print('You were robbing a house in the middle of the night when suddenly, the power went out.\n')
print('Try to find your way out of the house in the pitch black before the police get there. By the way, you\'re a very bad swimmer.\n')
print('Use \'w\' or \'n\' to go north, \'a\' to go west, \'s\' to go south, and \'d\' or \'e\' to go east.\n')
while done == True:
    print()
    print(room_list[current_room][0])
    direction = input('Which direction do you want to go?')

    if direction.upper() == 'W' or direction.upper() == 'N' or direction.upper() == 'NORTH':
        next_room = room_list[current_room][1]
        if next_room == None:
            print('You can\'t go that way.')
        else:
            current_room = next_room

    elif direction.upper() == 'A' or direction.upper() == 'WEST':
        next_room = room_list[current_room][4]
        if next_room == None:
            print('You can\'t go that way.')
        else:
            current_room = next_room

    elif direction.upper() == 'S' or direction.upper() == 'SOUTH':
        next_room = room_list[current_room][3]
        if next_room == None:
            print('You can\'t go that way.')
        else:
            current_room = next_room

    elif direction.upper() == 'D' or direction.upper() == 'E' or direction.upper() == 'EAST':
        next_room = room_list[current_room][2]
        if next_room == None:
            print('You can\'t go that way.')
        else:
            current_room = next_room

    else:
        print('Not a valid direction.')

    if current_room == 2:
        print('You have drowned in the pool. Didn\'t you remember that you don\'t know how to swim? Better luck next time!')
        done = False
    if current_room == 0:
        print('You made it out!')
        done = False

    turns += 1
    if turns == 10:
        print('You took too long to escape and you have been caught by the police!')
        done = False
print('\nThat\'s a GG in the chat. Press the green button if you want to play again')
