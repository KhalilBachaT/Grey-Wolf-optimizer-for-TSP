import random as random
import math as math


# calculate distance

def Euclidien(x1, x2, y1, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

# initialize cities and calculate distances between them


def init_cities(nb_cities):
    cities = {}
    city = []
    for i in range(nb_cities):
        city.append(random.uniform(0, 100))
        city.append(random.uniform(0, 100))
        cities[i] = city
        city = []
    for j, c in cities.items():
        distance = []
        for i, c1 in cities.items():
            distance.append(Euclidien(c[0], c1[0], c[1], c1[1],))
        c.append(distance)
    return cities

# initialize Wolves with random positions
# change the number of wolves after I finished


def init_wolves(nb_wolf):
    wolves = {}
    wolf = []
    for w in range(nb_wolf):
        wolf.append(random.uniform(0, 100))
        wolf.append(random.uniform(0, 100))
        wolves[w] = wolf
        wolf = []
    return wolves

# consider the fitness function as distance between the wolf and the city


def fitness(city, wolves):
    wolves_dist = []
    alpha, beta, delta = [], [], []
    for w in wolves:
        distance = Euclidien(wolves[w][0], city[0], wolves[w][1], city[1])
        wolves[w].append(distance)
        distance = 0.0
    wolves_dist = sorted(wolves.items(), key=lambda x: x[1][3])
    alpha = wolves_dist[0]
    beta = wolves_dist[1]
    delta = wolves_dist[2]
    return wolves_dist, alpha, beta, delta
