from file_management import *


files_list = ["a", "b", "c", "d", "e", "f"]

for letter in files_list:
    f = read_file('input/'+ letter +'.txt')
    # f = read_file('input/b.txt')

    duration, nb_intersections, nb_streets, nb_cars, bonus_point, S, list_streets, list_cars = f

        # list_streets.append([begin_intersection, end_intersection, index_street, length])
    # print(list_cars)
    # print(list_streets)
    #print(f)

    # nb visit de chaque street
    nb_visit = [0]*nb_streets
    for car in list_cars:
        for street in car:
            nb_visit[street] += 1

    inter = []
    # initialisation
    for i in range(nb_intersections):
        inter.append(dict())

    for i in range(nb_streets):
        inte = list_streets[i][1]
        #print(inte,S[i])
        inter[inte][S[i]] = nb_visit[i]

    # pour chaque inter, quelles street y arrivent et combien de fois elles sont visitees

    #print(inter)

    out = dict()
    # initialisation
    for i in range(nb_intersections):
        out[i] =dict()

    #boucle sur les inters qui calcule le ratio de chaque rue
    for i in range(nb_intersections):
        incoming_streets = list(inter[i].keys())
        n_incoming_cars = [inter[i][street] for street in incoming_streets]
        
        total_cars = sum(n_incoming_cars)



        # min_visit
        for street in incoming_streets:
            if inter[i][street] == 0 and (total_cars==0):
                t=1
                out[i][street] = t
                
            else:
                if inter[i][street] != 0:
                    t = int(4*inter[i][street] / (total_cars +0.1)) +1
                    out[i][street] = t
            

  


    write_output(out,letter +'_frac.txt')










