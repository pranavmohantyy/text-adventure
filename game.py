import json
from colorama import Fore, Style

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
        if item in self.items:
            self.items.remove(item)

class Game:
    def __init__(self, story_file):
        self.rooms = self.load_story(story_file)
        self.current_room = self.rooms[0] if self.rooms else None

    def load_story(self, story_file):
        with open(story_file) as f:
            story = json.load(f)
        return [Room(r["name"], r["description"]) for r in story["rooms"]]

    def move(self, direction):
        new_room = self.current_room.get_room(direction)
        if new_room:
            self.current_room = new_room

    def play(self):
        while True:
            print(self.current_room.description)
            command = input("> ").strip().lower()
            if command in ["exit", "quit"]:
                break
            self.move(command)

if __name__ == '__main__':
    game = Game('story.json')
    game.play()