import doctest
import copy

competitor_list = []

class Competitor:
    """ A class representing a competitor in a food eating competition """

    # taking the weight class as a string, will be converted to multiplier using dictionary
    def __init__(self, food: float, weight_class: str) -> None:
        """
        Instantiates a competitor object.

        Parameters:
            food (float): quantity of food consumed by a competitor during the competition
            weight_class (str): weight class of the competitor

        #>>> player_1 = Competitor(5.0, 'featherweight')
        #>>> print(player_1)
        Competitor(5.0, featherweight)
        #>>> player_1 = Competitor(5.0, 'FeaTHErweighT')
        #>>> print(player_1)
        #Competitor(5.0, featherweight)
        #>>> player_1 = Competitor(5, 'featherweight')
        #Traceback (most recent call last):
        #...
        #AssertionError: argument passed to food parameter must be a non-negative float
        #>>> player_1 = Competitor(5.0, 'verybigweight')
        #Traceback (most recent call last):
        #...
        #AssertionError: argument passed to weight_class parameter must be a key in weight_class dictionary
        """

        # checking preconditions
        assert isinstance(food, float) and food >= 0, "argument passed to food parameter must be a non-negative float"
        # no need to check that it is string object, since all keys are strings
        assert weight_class.casefold() in weight_class_multipliers.keys(), "argument passed to weight_class parameter must be a key in weight_class dictionary"

        self._food = food
        self._weight_class = weight_class.casefold()

        # upon instantiation, add to list of competitors (tests populate list, and cannot prevent duplicates, so tests commented out)
        competitor_list.append(self)

    # trying to use signature for challenges, as Competitor, does not work
    def __eq__(self, other) -> bool:
        """
        Checks whether strings for competitor objects are equivalent.

        Returns:
             (bool): whether strings for competitor objects are equivalent

        #>>> player_1 = Competitor(8.0, 'strawweight')
        #>>> player_2 = Competitor(8.0, 'strawweight')
        #>>> player_1.__eq__(player_2)
        True
        #>>> player_3 = Competitor(8.0, 'featherweight')
        #>>> player_1.__eq__(player_3)
        #False
        #>>> player_3.__eq__(player_1)
        #False
        #>>> player_1.__eq__(player_2)
        #True
        """

        return self.__str__() == other.__str__()

    def __str__(self) -> str:
        """
        Outputs a string representation of the object.

        Returns:
            (str): string representation of the object

        #>>> player_1 = Competitor(5.0, 'featherweight')
        #>>> player_1.__str__()
        'Competitor(5.0, featherweight)'
        """

        return f"Competitor({self._food}, {self._weight_class})"

    # not sure if getter and setter function always need to be implemented, but for this code does not seem necessary

    # this function seems redundant, since same calculation is made in net score function, but needed to calculate deduction
    def calculate_raw_food_credits(self) -> float:
        """
        Calculates the quantity of raw food credits earned by the competitor during the competition.

        Returns:
            (float): quantity of raw food credits

        #>>> player_1 = Competitor(5.0, 'featherweight')
        #>>> player_1.calculate_raw_food_credits()
        #25.0
        #>>> player_1 = Competitor(10.0, 'heavyweight')
        #>>> player_1.calculate_raw_food_credits()
        #1.0
        """

        # using dictionary index to retrieve appropriate multiplier
        return self._food * weight_class_multipliers[self._weight_class]

    # not static method, since object in question must not be included in the count
    def score_deduction(self) -> float:
        """
        Calculates score deduction for competitor according to challenges competitors' results.

        Returns:
            (float): score deduction for a given competitor


        """

        # instantiate object to amass deduction points
        deduction = 0

        # same for all competitors
        deduction_multiplier = 0.2

        # update competitor list to remove self
        # NEED DEEPCOPY INSTEAD OF SIMPLE LINK TO EXISTING LIST, SINCE REMOVAL OF ELEMENT AFFECTS BOTH LISTS
        competitors_list = copy.deepcopy(competitor_list)
        competitors_list.remove(self)

        # iterate through list of competitor (in a better implementation, could have a class to contain said list)
        for competitor in competitors_list:
            # accumulating deduction, but instead of single looking at single competitor, considering many
            deduction += competitor.calculate_raw_food_credits() * deduction_multiplier

        return deduction

    def calculate_net_score(self) -> float:
        """
        Calculates net score of competitor based on raw score and deduction.

        Returns:
            (float): net score of competitor, after deduction

        # test does not work since list is global
        >>> you = Competitor(20.0, 'flyweight')
        >>> opponent = Competitor(10.0, 'strawweight')
        >>> competitor_list[0].calculate_net_score()
        170.0
        >>> competitor_list[1].calculate_net_score()
        110.0
        """

        # raw food credits minus the deduction, passing self as parameter outside of class, which seems like bad practice...
        net_score = self._food * weight_class_multipliers[self._weight_class] - self.score_deduction()

        # condition to avoid negative scores
        if net_score < 0:
            return 0

        return net_score

# global variable from which multipliers for different competitors are pulled
weight_class_multipliers = {
    'strawweight': 15,
    'flyweight': 10,
    'featherweight': 5,
    'lightweight': 1,
    'welterweight': 0.5,
    'heavyweight': 0.1
}

doctest.testmod()