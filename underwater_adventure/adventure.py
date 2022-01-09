from time import sleep

from .player import Player
from .translation import open_locale_file
from .world import start_room

player = Player(start_room)

verbs = {}


def setup(lang):
    with open_locale_file(lang, 'keywords/look') as f:
        for line in f:
            verbs[line.strip()] = player.look
    with open_locale_file(lang, 'keywords/push') as f:
        for line in f:
            verbs[line.strip()] = player.push
    with open_locale_file(lang, 'keywords/pull') as f:
        for line in f:
            verbs[line.strip()] = player.pull
    with open_locale_file(lang, 'keywords/pickup') as f:
        for line in f:
            verbs[line.strip()] = player.pickup
    with open_locale_file(lang, 'keywords/open') as f:
        for line in f:
            verbs[line.strip()] = player.open_exit
    with open_locale_file(lang, 'keywords/move') as f:
        for line in f:
            verbs[line.strip()] = player.move
    with open_locale_file(lang, 'keywords/inventory') as f:
        for line in f:
            verbs[line.strip()] = player.inventory
    with open_locale_file(lang, 'keywords/use') as f:
        for line in f:
            verbs[line.strip()] = player.use


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
