import random


class String(object):
    def __init__(self, name=None, value='', select=[], reference=None, mutable=True):
        self.value=value
        self.mutable = mutable
        self.select = select

    def random(self):
        if self.mutable is False:
            return self.value.encode(encoding="utf-8")
        if len(self.select) > 0:
            return random.choice(self.select)
        return 

class int32(object):

    def __init__(self, name=None, value=0, min=-2147483648, max=2147483647, select=[], reference=None, mutable=True, littleEndian=True):
        self.value=value
        self.min = min
        self.max = max
        self.position = self.min
        self.mutable = mutable
        if littleEndian is True:
            self.endian = "little"
        else:
            self.endian = "big"
        # TODO
        if reference:
            self.value = len(reference)
        # TODO
        self.odds = [0, 1, 128, 256, 512, 1024, 2048, 4096]
    
    def _to_bytes(self, value):
        return value.to_bytes(4, byteorder=self.endian, signed=True)
    
    # TODO: How set sequence to Distributed fuzz
    def sequence(self):
        temp = self.position
        self.position += 1
        return self._to_bytes(temp)
    
    def random(self):
        if self.mutable is False:
            return self._to_bytes(self.value)
        return self._to_bytes(random.randint(self.min, self.max))


class Block(object):
    def __init__(self, blocks=None):
        if blocks is None:
            self.blocks = []
        else:
            self.blocks = blocks
    
    def random(self):
        data = b''
        for block in self.blocks:
            data += block.random()
        return data

class Choice(object):
    pass

class Repeater(object):
    pass

ggg = Block(blocks = [
    int32(min=1, max=10),
    int32(min=1, max=10),
    int32(min=1, max=10)
])

print(ggg.random())