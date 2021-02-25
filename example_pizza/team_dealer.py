import random

class TeamDealer():
    def __init__(self, nb_team2, nb_team3, nb_team4):
        self.dict_remaining_teams_by_nbpeople = {
            2:nb_team2,
            3:nb_team3,
            4:nb_team4,
        }
        
    def has_team(self):
        return len(self.dict_remaining_teams_by_nbpeople) > 0

    def sanity_check(self):
        for nb_people, nb_teams_remaining in list(
            self.dict_remaining_teams_by_nbpeople.items()
        ):
            if nb_teams_remaining == 0:
                del(self.dict_remaining_teams_by_nbpeople[nb_people])

    def pop_random(self):
        nbpeople = random.choice(list(self.dict_remaining_teams_by_nbpeople.keys()))
        
        self.dict_remaining_teams_by_nbpeople[nbpeople] -= 1
        self.sanity_check()
        return nbpeople

    def pop_smallest(self):
        nbpeople = sorted(self.dict_remaining_teams_by_nbpeople.keys())[0]
        self.dict_remaining_teams_by_nbpeople[nbpeople] -= 1
        self.sanity_check()
        return nbpeople

    def pop_largest(self):
        nbpeople = sorted(self.dict_remaining_teams_by_nbpeople.keys())[-1]
        self.dict_remaining_teams_by_nbpeople[nbpeople] -= 1
        self.sanity_check()
        return nbpeople
    
    def pop_teamnb(self, nbpeople):
        if nbpeople not in self.dict_remaining_teams_by_nbpeople:
            raise Exception(f"no more team of {nbpeople}")
        self.dict_remaining_teams_by_nbpeople[nbpeople] -= 1
        self.sanity_check()
        return nbpeople