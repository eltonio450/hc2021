def compute_score(list_results, dict_set_ingredientsnumber_by_indexpizza):
    score = 0
    for result in list_results:
        s = None
        for indexpizza in result:
            if s is None:
                s = dict_set_ingredientsnumber_by_indexpizza[indexpizza]
            else:
                s = s.union(dict_set_ingredientsnumber_by_indexpizza[indexpizza])
        score += len(s)**2
    return score