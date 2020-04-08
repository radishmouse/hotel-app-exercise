#hotel app

EMPTY_ROOM = {}

hotel = {
    '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309,
	   'prepaid': True,
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890,
	   'prepaid': False
        }
    },
    '105': {},
}

def is_vacant(which_hotel, which_room):
	if which_hotel[which_room] == EMPTY_ROOM:
		return True
	else:
		return False

def check_in(which_hotel, which_room, new_guest):
	if is_vacant(which_hotel, which_room):
		which_hotel[which_room]['guest'] = new_guest

def check_out(which_hotel, which_room):
	if not is_vacant(which_hotel, which_room):
		guest = which_hotel[which_room]['guest']
		which_hotel[which_room] = EMPTY_ROOM
		return guest

def print_status(which_hotel):
    # Printing the room status
    print('-----------------------------------')
    print('----------- hotel status ----------')
    print('-----------------------------------')
    for room_number in which_hotel.keys():
        # The room_number variable will be a 
        # string, like '101' or '103'
        if is_vacant(which_hotel, room_number):
            print(f'{room_number} is vacant')
        else:
            print(f'{room_number} is occupied by {which_hotel[room_number]["guest"]["name"]}')

    print('-----------------------------------')
    print('\n\n')

print_status(hotel)
input()
guest = {
	'name': 'Angela Moss',
	'phone': '333-3333',
	'prepaid': True
}
check_in(hotel, '103', guest)
print_status(hotel)
input()
another_guest = check_out(hotel, '101')
print(f'{another_guest["name"]} has checkd out\n\n')
print_status(hotel)
