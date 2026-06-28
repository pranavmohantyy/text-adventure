import json

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

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'connections': {direction: room.name for direction, room in self.connections.items()},
            'items': self.items,
            'npcs': [npc.name for npc in self.npcs],
            'locked': self.locked,
            'lock_item': self.lock_item
        }

    @classmethod
    def from_dict(cls, data):
        room = cls(data['name'], data['description'])
        room.connections = {direction: None for direction in data['connections'].keys()}
        room.items = data['items']
        room.npcs = []  # assuming NPCs need to be added later
        room.locked = data['locked']
        room.lock_item = data['lock_item']
        return room

def save_game_state(rooms, filename):
    with open(filename, 'w') as f:
        json.dump({room.name: room.to_dict() for room in rooms}, f)

def load_game_state(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return {name: Room.from_dict(room_data) for name, room_data in data.items()}
