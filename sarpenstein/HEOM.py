import math
from .models import *
from django.db.models import Max, Min

class HEOMClass():
    """HEOMClass is the class that holds all the functions that will be used to perform the ranking."""

    def __init__(self, cost_max, cost_min):
        # Get the maximum and minimum costs from the database
        self.MaxCost = cost_max
        self.MinCost = cost_min
        self.CostDiff = int(self.MaxCost) - int(self.MinCost)


    # This function is called when the attribute's type is categorical
    def overlap(self, x, y):
        if x == y:
            return 0
        else:
            return 1

    # This function is called when the attribute's type is NOT categorical
    def rn_diff(self, x, y):
        diff = int(x) - int(y)
        score = float(diff) / float(self.CostDiff)
        return score

    # This is the initial function called to add up the rank scores for each category
    def h_i(self, x, y, i):
        if x is None or y is None:
            return 1
        elif i == "categorical":
            return self.overlap(x, y)
        elif i == "regular":
            return self.rn_diff(x, y)

    # This takes in the two lists containing the rank scores and returns the HEOM score for the search query
    def heom(self, score_list):
        if len(score_list) != 6:
            raise Exception('score list should contain 6 category scores', score_list)

        ans = 0.0
        # loop through the two lists containing the rank ascores
        for item in score_list:
            ans += math.pow(item, 2)
        return math.sqrt(ans)
