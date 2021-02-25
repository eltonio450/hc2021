from file_management import *
import numpy as np


# f = read_file('input/a.txt')
f = read_file('input/b.txt')

duration, nb_intersections, nb_streets, nb_cars, bonus_point, S, list_streets, list_cars = f

    # list_streets.append([begin_intersection, end_intersection, index_street, length])
# print(list_cars)
# print(list_streets)
print(f)

# nb visit de chaque street
nb_visit = [0]*nb_streets
for car in list_cars:
    print('hey')
    for street in car:
        nb_visit[street] += 1

inter = []

for i in range(nb_intersections):
    inter.append(dict())

for i in range(nb_streets):
    inte = list_streets[i][1]
    print(inte,S[i])
    inter[inte][S[i]] = nb_visit[i]

# pour chaque inter, quelles street y arrivent et combien de fois elles sont visitees

print(inter)

#boucle sur les inters qui calcule le ratio de chaque rue
for i in range(nb_intersections):
    rues = list(inter[i].keys())
    times =[inter[i][r] for r in rues]
    tot = sum(times)
    print(inter[i])
    print(times)
    for street in rues:
        t = int(3*inter[i][street] / (tot +0.1)) +1
        print(street,t)










