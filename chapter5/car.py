class Car(object):

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = 0

    def turn_right(self):
        self.direction += 1
        self.direction = self.direction % 4

    def turn_left(self):
        self.direction -= 1
        self.direction = self.direction % 4

    def move(self, distance):
        if self.direction == self.NORTH:
            self.y += distance
        elif self.direction == self.SOUTH:
            self.y -= distance
        elif self.direction == self.EAST:
            self.x += distance
        else:
            self.x -= distance

    def position(self):
        return (self.x, self.y)
