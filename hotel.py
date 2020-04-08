#hotel app

hotel = {
    '101': '',
    '102': '',
    '103': '',
    '104': '',
    '105': '',
}

elliot = {
    'occupant_name': 'Elliot',
    'phone_number': 8675309,
    'has_prepaid': True
}
# guest is "checking in"
hotel['101'] = elliot

# customer = {}
# name = input('What is the name of the guest? ')
# customer['name'] = name

# hotel['104'] = customer


# Printing the room status
for room_number in hotel.keys():
    # The room_number variable will be a 
    # string, like '101' or '103'
    if hotel[room_number] == '':
        print(f'{room_number} is vacant')
    else:
        print(f'{room_number} is occupied by {hotel[room_number]["occupant_name"]}')

# For any one room, you should store:
# - occupant name
# - phone number
# - has prepaid

