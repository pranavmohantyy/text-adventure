# Text Adventure Game

## Custom Story Format

To create your own story, you'll need to write a JSON file that defines the rooms, items, and NPCs. Below is the structure you should follow:

```json
{
  "rooms": [
    {
      "name": "Room Name",
      "description": "A brief description of the room.",
      "connections": {
        "north": "Other Room Name",
        "east": "Another Room Name"
      },
      "items": ["item1", "item2"],
      "npcs": ["npc1"],
      "locked": false,
      "lock_item": null
    }
  ],
  "items": [
    {
      "name": "item1",
      "description": "A description of the item."
    }
  ],
  "npcs": [
    {
      "name": "npc1",
      "description": "A description of the NPC."
    }
  ]
}
```

### Example

Here's an example of a simple story:

```json
{
  "rooms": [
    {
      "name": "Hallway",
      "description": "A long, dark hallway.",
      "connections": {
        "north": "Kitchen",
        "south": "Living Room"
      },
      "items": ["key"],
      "npcs": ["ghost"],
      "locked": true,
      "lock_item": "key"
    },
    {
      "name": "Kitchen",
      "description": "A messy kitchen.",
      "connections": {},
      "items": [],
      "npcs": [],
      "locked": false,
      "lock_item": null
    }
  ],
  "items": [
    {
      "name": "key",
      "description": "A rusty old key."
    }
  ],
  "npcs": [
    {
      "name": "ghost",
      "description": "A spooky ghost."
    }
  ]
}
```

Happy adventuring!