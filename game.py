class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []
        self.npcs = []

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

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []
        self.health = 100

    def move(self, direction):
        new_room = self.current_room.get_room(direction)
        if new_room:
            self.current_room = new_room

    def attack(self, npc):
        if npc in self.current_room.npcs:
            npc.health -= 10
            if npc.health <= 0:
                self.current_room.npcs.remove(npc)

class NPC:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, player):
        player.health -= 10
