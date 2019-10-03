from .world import darkness, flashlight

vowels = ['a', 'e', 'i', 'o', 'u']


class Player:
    def __init__(self, location):
        self.location = location
        self.item_list = []

    def look(self, words):
        if not words:
            return self.location.look()
        else:
            # Find object
            for w in words:
                for e in self.location.exits:
                    if e.name == w:
                        return e.look()
                # room objects
                for o in self.location.objects:
                    if o.name == w:
                        return o.look()
                for i in self.item_list:
                    if i.name == w:
                        return i.look()

            return 'I\'m not sure what you\'re referring to.'

    def push(self, words):
        pass

    def pull(self, words):
        pass

    def pickup(self, words):
        for o in self.location.objects:
            if o.name in words:
                if o.gettable:
                    self.item_list.append(o)
                    self.location.objects.remove(o)
                    return 'Taken'
                else:
                    return o.pickup_description or 'I can\'t pick that up.'
            for sub_obj in o.objects:
                if sub_obj.name in words:
                    self.item_list.append(sub_obj)
                    o.objects.remove(sub_obj)
                    return 'Taken'
        else:
            return 'I don\'t see that here'

    def open_exit(self, words):
        pass

    def move(self, words):
        if flashlight not in self.item_list and self.location != darkness:
            self.location = darkness
            return darkness.look()
        for e in self.location.exits:
            for n in e.name:
                if n in words:
                    if not e.locked:
                        self.location = e.room
                        return e.room.look()
                    else:
                        return e.locked_description

    def inventory(self, words):
        if len(self.item_list) > 0:
            ret = 'You\'re carrying\n'
            for i in self.item_list:
                name = i.inventory_name or i.name
                ret += '{} {}\n'.format('an' if name[0] in vowels else 'a',
                                        name)
            return ret
        else:
            return 'You\'re not carrying anything.'

    def use(self, words):
        for i in self.item_list + self.location.objects:
            if i.name in words:
                item = i
                words.remove(item.name)
                break
        else:
            item = None

        targets = (self.item_list + self.location.objects +
                   self.location.exits)
        target = None
        for t in targets:
            if isinstance(t.name, str):
                names  = [t.name]
            else:
                names = t.name
            for n in names:
                if n in words:
                    target = t
                    words.remove(n)
                    break
            if target:
                break

        if target:
            return target.use(item) or item.use(target)
        if item:
            return item.use(self.location)
        return 'I don\'t see that here'
