class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []

    def connect(self, direction, room):
        self.connections[direction] = room

    def get_room(self, direction):
        return self.connections.get(direction)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction):
        new_room = self.current_room.get_room(direction)
        if new_room:
            self.current_room = new_room
        else:
            print("You can't go that way.")

    def take_item(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print(f"You took {item_name}.")
                return
        print("Item not found.")

    def drop_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.current_room.add_item(item)
                self.inventory.remove(item)
                print(f"You dropped {item_name}.")
                return
        print("You don't have that item.")

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description