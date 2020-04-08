
# Hotel App

Here is an example of a dictionary that can be used to manage the occupants of a hotel.

```
hotel = {
    '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890           
        }
    },
    '105': {},
}
```

Feel free to customize the structure as you see fit!


## Small: Single hotel


The goal of the small exercise is to get practice with the syntax for querying and manipulating the data in a single, nested dictionary.

Write functions to:

- `is_vacant(which_hotel, '101')`
    - check if a room is occupied
- `check_in('101', guest_dictionary)`
    - assign a person to a room
- `check_out('101')`
    - returns the person dictionary in that room

Please look back at any notes or slides for how to perform any of these actions.

## Medium: three hotels

First, create a list of hotel dictionaries. They should contain at least 3 identical dictionaries (like the one in the example above).

Create a `while True` loop to show the following menu:

```
1. Print hotel room status
2. Check in customer
3. Check out customer
4. Quit

- When printing, show all rooms for all hotels and the name of the occupant, if there is one.
- When checking a customer in, make sure to choose a hotel as well as a room.
- Do not let a customer check into an occupied room.
- If the room is unoccupied, prompt for each piece of information (name, cell, etc.)
- upon check out, print out whether or not the customer has paid

```

## Medium: add/remove hotels

Add more options to your main menu.

Provide options to open a new hotel or close an existing hotel.

## Large: saving multiple hotel room info to file

Add menu options for:

- saving room info
- load room info

When you `save_room_info()`, write the `hotel` variable to a JSON file.

When you `load_room_info()`, read the data out of the JSON file.

Check in/out a few customers and then save the room data to a file.

Quit your python program and start it again.

Load the data from a file.

Make sure to `print()` the room status to confirm that you've loaded 

---

BONUS

- each room should have a 'bed_type' key whose values are one of the following:
    - 'king'
    - 'queen'
    - 'double twin'
- add a `request_room_type()` function that accepts a room type string
    - it should return the room number of a vacant room of that type
    - or it should return `None` if there are no rooms of that type available
- add a "pet_friendly" ammenity.
    - add a function to `request_pet_friendly()` room
    - if a customer checks into a pet friendly room, prompt for the name of the pet