class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}

    def connect(self, direction, room):
        self.connections[direction] = room

    def get_room(self, direction):
        return self.connections.get(direction)

class Player:
    def __init__(self, start_room):
        self.current_room = start_room

    def move(self, direction):
        new_room = self.current_room.get_room(direction)
        if new_room:
            self.current_room = new_room
        else:
            print("You can't go that way.")

if __name__ == '__main__':
    living_room = Room("Living Room", "A cozy living room.")
    kitchen = Room("Kitchen", "A kitchen with a strange smell.")
    living_room.connect("east", kitchen)
    kitchen.connect("west", living_room)

    player = Player(living_room)

    while True:
        print(f"You are in the {player.current_room.name}. {player.current_room.description}")
        command = input("Enter a direction (north/south/east/west): ").strip().lower()
        player.move(command)
