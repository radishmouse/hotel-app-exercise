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

# Printing the room status
for room_number in hotel.keys():
    # The room_number variable will be a 
    # string, like '101' or '103'
    if is_vacant(hotel, room_number):
        print(f'{room_number} is vacant')
    else:
        print(f'{room_number} is occupied by {hotel[room_number]["guest"]["name"]}')

# For any one room, you should store:
# - occupant name
# - phone number
# - has prepaid

