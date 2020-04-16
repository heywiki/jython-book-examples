#listing 4-26
def step_to(factor, stop):
    step = factor
    start = 0
    while start <= stop:
        yield start
        start += step

for x in step_to(2, 10):
    print(x)
