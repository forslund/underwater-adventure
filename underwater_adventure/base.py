

class Base:
    def look(self):
        pass

    def push(self):
        pass

    def pull(self):
        pass

    def pickup(self):
        pass

    def use(self, target=None):
        return ""


class Thing(Base):
    def __init__(self, name=None):
        self.name = name or 'thing'
        self.objects = []
        self.description = 'It\'s a thing'
        self.gettable = False
        self.room_description = ''
        self.pickup_description = ''
        self.inventory_name = ''

    def look(self):
        return ' '.join([self.description] +
                        [o.room_description for o in self.objects])


class Room(Base):
    def __init__(self, name=''):
        super().__init__()
        self.name = name
        self.exits = []
        self.objects = []
        self.description = "The room is empty"
        self.brief_description = "An empty room"
        self.visited = False

    def look(self):
        description = ' '.join([self.description] +
                               [o.room_description for o in self.objects
                                if o.room_description])

        description += '\n' + '\n'.join([e.description for e in self.exits])
        return description


class Exit(Base):
    def __init__(self, room, name, description=None, locked=False):
        self.room = room
        self.name = name
        self.locked = locked
        self.unlocked_by = None
        self.unlock_description = ""
        self.locked_description = 'It\'s locked'

        if description:
            self.description = description

    def key(self, thing):
        self.unlocked_by = thing

    def use(self, thing=None):
        if thing and thing == self.unlocked_by:
            self.locked = False
            return self.unlock_description
        elif self.locked:
            return '{} can\'t unlock that'.format(thing.name)
        else:
            return '{} can\'t lock that'.format(thing.name)

    def look(self):
        return str(self)

    def __str__(self):
        return self.description

