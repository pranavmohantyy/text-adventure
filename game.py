class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []
        self.npcs = []
        self.locked = False
        self.lock_item = None

    def connect(self, direction, room):
        self.connections[direction] = room

    def get_room(self, direction):
        return self.connections.get(direction)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def add_npc(self, npc):
        self.npcs.append(npc)

    def lock(self, item):
        self.locked = True
        self.lock_item = item

    def unlock(self, item):
        if item == self.lock_item:
            self.locked = False
            self.lock_item = None

    def is_locked(self):
        return self.locked

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction):
        next_room = self.current_room.get_room(direction)
        if next_room:
            if next_room.is_locked():
                print("The door is locked.")
                return
            self.current_room = next_room
        else:
            print("You can't go that way.")

    def pick_up(self, item):
        self.current_room.remove_item(item)
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            if self.current_room.is_locked() and item == self.current_room.lock_item:
                self.current_room.unlock(item)
                print("You unlocked the door!")
            else:
                print("You can't use that here.")
        else:
            print("You don't have that item.")