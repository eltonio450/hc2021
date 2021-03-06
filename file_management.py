from collections import defaultdict

def create_dict_streets_by_intersection(list_streets):
    dict_streets_by_intersection = defaultdict(lambda: dict(list_streetid_before=[], list_streetid_after=[]))
    for begin_intersection, end_intersection, index_street, length in list_streets:
        dict_streets_by_intersection[begin_intersection]["list_streetid_after"].append(index_street)
        dict_streets_by_intersection[end_intersection]["list_streetid_before"].append(index_street)
    return dict_streets_by_intersection

class TwoWayDict(dict):
    def __setitem__(self, key, value):
        # Remove any previous connections with these values
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

    def __len__(self):
        """Returns the number of connections"""
        return dict.__len__(self) // 2

def read_file(filepath):
    with open(filepath, 'r') as filecontent:
        firstline = filecontent.readline()
        duration, nb_intersections, nb_streets, nb_cars, bonus_point = list(map(int, firstline.strip().split(' ')))
        
        accu_street = 0
        twowaydict_indexstreet_streetname = TwoWayDict()
        list_streets = []
        for _ in range(nb_streets):
            line = filecontent.readline()
            begin_intersection, end_intersection, street_name, length = line.strip().split(' ')
            if street_name not in twowaydict_indexstreet_streetname:
                twowaydict_indexstreet_streetname[street_name] = accu_street
                accu_street += 1
            index_street = twowaydict_indexstreet_streetname[street_name]
            begin_intersection, end_intersection, length = list(map(int, [begin_intersection, end_intersection, length]))
            list_streets.append([begin_intersection, end_intersection, index_street, length])
        list_cars = []
        for _ in range(nb_cars):
            line = filecontent.readline()
            nb_streets_to_drive, *list_streets_for_car = line.strip().split(' ')
            list_streets_id = [twowaydict_indexstreet_streetname[street] for street in list_streets_for_car]
            list_cars.append(list_streets_id)
    return (duration, nb_intersections, nb_streets, nb_cars, bonus_point, twowaydict_indexstreet_streetname, list_streets, list_cars)

def write_output(dict_dict_time_by_street_by_intersectionid, filepath):
    with open(filepath, 'w') as output:
        firstline = f"{len(dict_dict_time_by_street_by_intersectionid)}\n"
        output.write(firstline)
        for intersection in dict_dict_time_by_street_by_intersectionid:
            output.write(f"{intersection}\n")
            nb_streets = len(dict_dict_time_by_street_by_intersectionid[intersection])
            output.write(f"{nb_streets}\n")
            for streetname, value in dict_dict_time_by_street_by_intersectionid[intersection].items():
                output.write(f"{streetname} {value}\n")