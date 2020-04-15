from car import Car

def test_car():
    c = Car()
    c.turn_right()
    c.move(5)
    assert (5, 0) ==  c.position()

    c.turn_left()
    c.move(3)

    assert (5, 3) == c.position()
    print c.position();

if __name__ == '__main__':
    test_car()
