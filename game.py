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
        next_room = self.current_room.get_room(direction)
        if next_room:
            self.current_room = next_room

class NPC:
    def __init__(self, name, dialogues):
        self.name = name
        self.dialogues = dialogues
        self.dialogue_index = 0

    def talk(self):
        line = self.dialogues[self.dialogue_index]
        self.dialogue_index = (self.dialogue_index + 1) % len(self.dialogues)
        return line