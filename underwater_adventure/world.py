from .base import Room, Thing, Exit


class Weld(Thing):
    def use(self, target):
        if target.name == 'knife':
            self.gettable = True
            self.description = ("An old Lincoln Welding machine."
                "It's in surprisingly good condition for a thing that's been "
                "submerged for this long. Unfortunately it's not usuable in "
                "water.")
            return ("Using the table knife the screws are removed one by one "
                    "until the weld is free to be moved.")
        else:
            return "That doesn't work"

weld = Weld()
weld.name = 'weld'
weld.description = ("An old weld. It's in surprisingly good condition for a "
    "thing that's been submerged for this long. Unfortunately it's not "
    "usuable in water. It has been secured to a wall using a couple of flat "
    "head screws.")
weld.room_description = "In a cuboard you see an old weld."
weld.pickup_description = "It's still stuck to the wall."

class OxygenTube(Thing):
    def use(self, target):
        if target.name == 'start' or target == hatch:
            air_pocket = Thing()
            air_pocket.room_description = "A pocket of air has formed around the hatch."
            # Add the air to the room description
            start_room.objects.append(air_pocket)
            # Now that there is air around the hatch make the lock weldable
            hatch.key(weld)
            return ("The oxygen is released an form an air pocket around the "
                    "hatch.")
        elif target.name == 'captain':
            return "There's alrady a pocket of air in this room."
        else:
            return "No, the gas will likely just leak away here."

class Hatch(Exit):
    def use(self, thing=None):
        if thing == oxygen:
            return oxygen.use(self)
        if thing and thing == self.unlocked_by:
            self.locked = False
            return self.unlock_description
        elif self.locked:
            return '{} can\'t unlock that'.format(thing.name)
        else:
            return '{} can\'t lock that'.format(thing.name)

outside = Room()
outside.description = (
    "The sun glimers far above, you are finally free.\n\n"
    "As you slowly asend towards the surface you look down onto the ship that "
    "trapped you and caused such claustrophobia. From the outside it looks "
    "quite serene.\n\n"

    "You tear your eyes from it and focus on the ever closer surface, a few "
    "bubbles escape as you relieved laugh into your mask.\n\n"
    "...")

start_room = Room('start')
start_room.description = ("It is dark but a Bluish light filters in through a "
    "small round window. The room is colorless and the walls seem to be made "
    "of metal.")

corridor = Room()
corridor.description = ("The corridor is dark, with very little decoration. "
    "All along the corridors are bulkheads similar to the one you entered "
    "through. At the far end there is a stairwell.")

captains_quarters = Room('captain')
captains_quarters.description = ("A sligthly bigger room than the ones below "
                                 "deck. with a bolted down desk centrally "
                                 "located. Debris on the floor looks like "
                                 "they once were books, now a fragile gray "
                                 "mass.\n\n"

                                 "In the ceiling there is a small pocket off "
                                 "air.")

desk = Thing()
desk.name = 'desk'
desk.room_description = ''
desk.description = 'The desk is bolted down to the floor.'

oxygen = OxygenTube()
oxygen.name = 'oxygen'
oxygen.inventory_name = "Oxygen tank"
oxygen.description = 'A tube of Pure O²'
oxygen.room_description = 'Under the desk lies an oxygen tank'
desk.objects.append(oxygen)

bottle = Thing()
bottle.name = "bottle"
bottle.inventory_name = "Ship in a bottle"
bottle.room_description = "An old ship in a bottle floats near the ceiling."
bottle.description = ("It's curious how this ship has fared better than the "
                      "one I'm currently in...")
captains_quarters.objects.append(desk)
captains_quarters.objects.append(bottle)

steering_hut = Room()
steering_hut.description = ("By the look of it this was the bridge, was "
                            "being the operative word the cramped space has "
                            "been crushed down. The rear of the room seems "
                            "pretty much unharmed and an impressive rack of "
                            "controls and panels are slowly rusing in the "
                            "salty water.")

controls = Thing('controls')
controls.description = ("None of the levers move and none of the lights are "
                        "on.\n\n"

                        "Well apparently this sunken ship isn't in mint "
                        "condition.")

panels = Thing('panels')
panels.description = "The needles in these gauges are all perfectly still."
steering_hut.objects.append(controls)
steering_hut.objects.append(panels)


engine_room = Room()
engine_room.description = ("A heap of rusting machinery. the water almost "
                           "feels dirty.")
engine_room.objects.append(weld)

galley = Room()
galley.description = ("The ship's galley, the floor is covered by debris, "
                      "but along the wall pots and cantines are still "
                      "standing even if they are in a state of disarray. "
                      "The stove is rusted and has likely fried it's last "
                      "egg. The tubing for the gas is the only thing that "
                      "looks to be in decent shape.")

drawer = Thing()
drawer.name = 'drawer'
drawer.description = "It's a mess."
drawer.room_description = "A drawer in one of the tables are slightly open."
galley.objects.append(drawer)

table_knife = Thing()
table_knife.name = 'knife'
table_knife.inventory_name = 'Table knife'
table_knife.description = "A very dull knife with a flat edge."""
table_knife.room_description = ("The only thing in decent shape in the drawer "
                                "is a table knife.")

drawer.objects.append(table_knife)

plaque = Thing()
plaque.name = "plaque"
plaque.description = ("An old motivational poster.\n\n"

                      "U.S. Marines FIRST to fight in France for freedom!\n\n"
                      )
plaque.room_description = ("Beside one of the bulkheads hangs a large "
                           "plaque, something in a corner reflects your "
                           "flashlight briefly.")

key = Thing()
key.name = "key"
key.gettable = True
key.description = "The letter C is engraved on it."
key.room_description = "Looking closer you notice a key stuck in behind it."

corridor.objects.append(plaque)
plaque.objects.append(key)
corridor.exits.append(Exit(start_room, ['bulkhead', 'exit', 'dark'],
                           'There is an open bulkhead leading to a dark room.'))
corridor.exits.append(
    Exit(galley, ['galley', 'kitchen'],
         'Another bulkhead leads to something looking like a galley.'))
corridor.exits.append(
    Exit(steering_hut, ['bridge', 'steering hut', 'steering', 'up'],
         'Up the stairs there seem to be a steering hut.'))
corridor.exits.append(
    Exit(engine_room, ['engine', 'down'],
         'Down the stairs is the engine room.'))

galley.exits.append(
    Exit(corridor, ['corridor', 'door', 'back'],
         'A door leading back out into the corridor'))

steering_hut.exits.append(
    Exit(corridor, ['corridor', 'down'],
         'A stair leads down into a corridor'))

locked_door = Exit(captains_quarters, ['captain', 'quarters', 'door'],
                   'A door labeled "Captain"', locked=True)
locked_door.unlock_description = "Surprisingly the key turns smoothly, unlocking the door."
locked_door.key(key)
steering_hut.exits.append(locked_door)

captains_quarters.exits.append(Exit(steering_hut,
                                    ['steering', 'hut', 'door', 'back'],
                                    'A door leads back out to the steering hut.'))

engine_room.exits.append(
    Exit(corridor, ['corridor', 'up', 'back', 'door'],
         'A door leading back out to the stairs leading back to the the corridor.'))

hatch = Hatch(outside, ['hatch', 'up'],
              'There is a heavy hatch in the ceiling', locked=True)
hatch.unlock_description = 'You burn through the locking mechanism with the weld.'
start_room.exits.append(hatch)
start_room.exits.append(Exit(corridor,
                             ['bulkhead', 'left', 'corridor', 'darkness'],
                             'A bulkhead leaving into darkness.'))
thing = Thing()
thing.room_description = 'There\'s a Thing in the corner.'
start_room.objects.append(thing)

flashlight = Thing('flashlight')
flashlight.inventory_name = 'flashlight that has never failed you.'
flashlight.description = "A trusty flashlight you've had since forever."
flashlight.room_description = 'A flashlight lies on the floor casting a cone of dim light.'
start_room.objects.append(flashlight)
flashlight.gettable = True


darkness = Room()
darkness.description = ("It is dark, you will likely need some sort of ",
                        "light to explore further\n\n"

                        "...you are likely to be eaten by a Grue...\n")
darkness.exits.append(Exit(start_room, ['bulkhead', 'exit', 'light', 'back'],
                           'There is an open bulkhead leading to a slightly less dark room.'))
