import random

class PizzaDealer():
    def __init__(self, nb_pizzas, list_indexpizza_by_tuple_ingredients):
        self.nb_pizzas_left = nb_pizzas
        self.list_indexpizza_by_tuple_ingredients = list_indexpizza_by_tuple_ingredients
    def has_pizza(self):
        return self.nb_pizzas_left > 0
    def pop_random(self):
        random_tuple_ingredients = random.choice(list(self.list_indexpizza_by_tuple_ingredients.keys()))
        pizzaindex = self.list_indexpizza_by_tuple_ingredients[random_tuple_ingredients].pop()
        if len(self.list_indexpizza_by_tuple_ingredients[random_tuple_ingredients]) == 0:
            del(self.list_indexpizza_by_tuple_ingredients[random_tuple_ingredients])
        return pizzaindex
