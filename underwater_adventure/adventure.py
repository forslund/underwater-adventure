from time import sleep

from .player import Player
from .world import start_room


player = Player(start_room)

verbs = {
    'look': player.look,
    'check': player.look,
    'inspect': player.look,
    'push': player.push,
    'pull': player.pull,
    'pick': player.pickup,
    'get': player.pickup,
    'take': player.pickup,
    'open': player.open_exit,
    'go': player.move,
    'enter': player.move,
    'swip': player.move,
    'inventory': player.inventory,
    'use': player.use,
    'unlock': player.use
}


def parse_input(sentence):
    verb = None
    words = sentence.split()
    # find verb
    for w in words:
        if w in verbs:
            verb = verbs[w]
            words.remove(w)
            break
    else:
        verb = None
    if verb:
        return verb(words)
    else:
        return player.move(words)


def introduction():
    print("""Wreck diving has always been a passion.

You just can't leave a sunken ship in this good condition alone. It's lure is
just too strong.\n""")
    sleep(5)
    print("""You dive down through the clear water alone inspecting the small
vessel from the outside finding a point of entry.\n""")
    sleep(5)
    print("There!\n")
    sleep(1)
    print("An open hatch!\n")
    sleep(1)
    print("""You drop your flashlight throughh the hatch illuminating a small room.
The room looks safe enough so you start to descend through the opening.

When you're just about through you feel a tug at your back and then you're
pushed down by the weight of the hatch.\n""")
    sleep(5)
    print("""Pushing at the hatch you realize a lock bolt has snapped into place.

You are trapped.\n\n""")


def simple_game_loop():
    inp = None
    introduction()
    print(player.location.look())

    while (inp != 'quit'):
        inp = input('\n>')
        response = parse_input(inp.lower())
        if response:
            print(response.strip())
