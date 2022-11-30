
from mas import *

if __name__ == '__main__' :
    print('OK')
    world = World()
    agents = [Agent(id = i) for i in range(5)]
    report, log = Simulator().run(world = world, agents = agents)
    Player().play(log = log)
