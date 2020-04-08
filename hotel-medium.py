#hotel app

EMPTY_ROOM = {}

hotel1 = {
    '101': {},
    '102': {},
    '103': {},
    '104': {},
    '105': {},
}
hotel2 = {
    '101': {},
    '102': {},
    '103': {},
    '104': {},
    '105': {},
}
hotel3 = {
    '101': {},
    '102': {},
    '103': {},
    '104': {},
    '105': {},
}

hotels = [hotel1, hotel2, hotel3]

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

# print_status(hotel)
# input()
# guest = {
# 	'name': 'Angela Moss',
# 	'phone': '333-3333',
# 	'prepaid': True
# }
# check_in(hotel, '103', guest)
# print_status(hotel)
# input()
# another_guest = check_out(hotel, '101')
# print(f'{another_guest["name"]} has checkd out\n\n')
# print_status(hotel)

def create_guest():
    name = input('Guest name: ')
    phone = input('Guest phone: ')
    prepay_str = input('Prepay? (y or n) ')
    prepay_str = prepay_str.lower()
    if prepay_str == 'y':
        prepaid = True
    else:
        prepaid = False

    guest = {
        'name': name,
        'phone': phone,
        'prepaid': prepaid
    }
    return guest

main_menu = '''
1. Print hotel room status
2. Check in customer
3. Check out customer
4. Quit
'''

while True:
    menu_choice = int(input(main_menu))
    if menu_choice == 1:
        for hotel in hotels:
            print_status(hotel)
    elif menu_choice == 2:
        guest = create_guest()
        while True:            
            hotel_id = int(input('Which hotel? '))
            try:
                hotel = hotels[hotel_id]
                break
            except IndexError:
                print('Invalid hotel id')
        while True:
            room_number = input('Which room number?')
            try:
                if is_vacant(hotel, room_number):
                    check_in(hotel, room_number, guest)
                    break
            except KeyError:
                print('Invalid room number')
    elif menu_choice == 3:
        while True:            
            hotel_id = int(input('Which hotel? '))
            try:
                hotel = hotels[hotel_id]
                break
            except IndexError:
                print('Invalid hotel id')
        while True:
            room_number = input('Which room number?')
            try:
                guest = check_out(hotel, room_number)
                print(f'{guest["name"]} has checked out\n\n')
                break
            except KeyError:
                print('Invalid room number')            

    elif menu_choice == 4:
        break

print('Thanks for using the hotel mgmt app!')