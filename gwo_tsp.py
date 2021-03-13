import random as random
import math as math
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import keyboard
import functions

# GWO algorithem for TSP


def GWO_TSP(map_cities, start, my_wolves, max_iter):
    map_cities_dynamic = {}
    wolves_updated = {}
    for i, w in my_wolves.items():
        wolves_updated[i] = w
    for i, m in map_cities.items():
        map_cities_dynamic[i] = m
    alpha_city = {}
    Tour = False
    start_city = map_cities[start]
    my_wolves_sorted = []
    r1, r2, C, A, alpha, beta, delta, direction, path, ll, X1, X2, X3 = [
    ], [], [], [], [], [], [], [], [], [], [], [], []
    a = 2
    i = 0
    r1.append(random.random())
    r1.append(random.random())
    A.append(2*a*r1[0]-a)
    A.append(2*a*r1[1]-a)
    path.append(start)
    del map_cities_dynamic[start]
    # loop with max number of iterations / cities / finish the tour
    # next posi is start in ll
    while (Tour != True) and (i < max_iter):
        # calculate the direction of each search wolf to the current city
        for k, w in my_wolves.items():
            r2.append(random.random())
            r2.append(random.random())
            C.append(2*r2[0])
            C.append(2*r2[1])
            direction.append(abs(C[0]*start_city[0]-w[0]))
            direction.append(abs(C[1]*start_city[1]-w[1]))
            w.append(direction)
            direction, C, r2 = [], [], []

        # calculate the fitness function and update α,β,δ
        my_wolves_sorted, alpha, beta, delta = functions.fitness(
            start_city, my_wolves)
        # update positions of OMEGA wolves
        for w in my_wolves.keys():
            if (w != alpha[0] and w != beta[0] and w != delta[0]):
                # calculate X1 = xa - a*da, X2, X3
                X1.append(alpha[1][0]-A[0]*alpha[1][2][0])
                X1.append(alpha[1][1]-A[1]*alpha[1][2][1])
                X2.append(beta[1][0]-A[0]*beta[1][2][0])
                X2.append(beta[1][1]-A[1]*beta[1][2][1])
                X3.append(delta[1][0]-A[0]*delta[1][2][0])
                X3.append(delta[1][1]-A[1]*delta[1][2][1])
                my_wolves[w][0] = (X1[0]+X2[0]+X3[0])/3
                my_wolves[w][1] = (X1[1]+X2[1]+X3[1])/3
                # update Xt (current position) => Xt+1 (next position)
        r1, r2, C, A, X1, X2, X3 = [], [], [], [], [], [], []

        # update parameters
        r1.append(random.random())
        r1.append(random.random())
        r2.append(random.random())
        r2.append(random.random())
        a = 2*(1-(i/10))
        A.append(2*a*r1[0]-a)
        A.append(2*a*r1[1]-a)
        C.append(2*r2[0])
        C.append(2*r2[1])

        # find the next city
        for n, nxt in map_cities_dynamic.items():
            dist = functions.Euclidien(
                alpha[1][0], nxt[0], alpha[1][1], nxt[1])
            alpha_city[n] = dist
        ll = sorted(alpha_city.items(), key=lambda x: x[1])

        # delete the city founded from map_cities_dynamic and add it to path
        if len(map_cities_dynamic) != 0:
            del map_cities_dynamic[ll[0][0]]
            path.append(ll[0][0])
        else:
            Tour = True
            break
        start_city = map_cities[ll[0][0]]
        ll = []
        alpha_city = {}

        i += 1
    return path, wolves_updated
