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

def read_file(filename):
    ingredient_number = 0
    twowaydict_ingredientnumber_ingredientname = TwoWayDict()
    dict_set_ingredientsnumber_by_indexpizza = dict()
    
    with open(filename, 'r') as contentfile:
        firstline = contentfile.readline()
        nb_pizzas, nb_team2, nb_team3, nb_team4 = list(map(int, firstline.strip().split(' ')))
        for index_pizza in range(nb_pizzas):
            this_pizza_line = contentfile.readline()
            nb_ingredients, *list_ingredients = this_pizza_line.split(' ')
            for ingredient in list_ingredients:
                if ingredient in twowaydict_ingredientnumber_ingredientname:
                    continue
                twowaydict_ingredientnumber_ingredientname[ingredient] = ingredient_number
                ingredient_number += 1
            dict_set_ingredientsnumber_by_indexpizza[index_pizza] = set([
                twowaydict_ingredientnumber_ingredientname[ingredient]
                for ingredient in list_ingredients])
    return (
        nb_pizzas, nb_team2, nb_team3, nb_team4, ingredient_number,
        twowaydict_ingredientnumber_ingredientname,
        dict_set_ingredientsnumber_by_indexpizza
    )

def write_results_in_output(results, filename):
    with open(filename, "w") as outputfile:
        for list_index_pizza in results:
            nb_pizzas = len(list_index_pizza)
            outputfile.write(" ".join(map(str, [nb_pizzas, *list_index_pizza])) + "\n")
