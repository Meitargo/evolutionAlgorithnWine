import random
import numpy as np

from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator

NUM_ITEMS = 20


class KnapsackEvaluator(SimpleIndividualEvaluator):
    """
    Evaluator class for the Knapsack problem, responsible of defining a fitness evaluation method and evaluating it.
    In this example, fitness is the total price of the knapsack

    Attributes
    -------
    items: dict(int, tuple(int, float))
        dictionary of (item id: (weights, prices)) of the items
    """

    def __init__(self, items=None, max_weight=30):
        super().__init__()

        if items is None:
            # Generate ramdom items for the problem (keys=weights, values=values)
            items = {i: (random.randint(1, 10), random.uniform(0, 100)) for i in range(NUM_ITEMS)}
        self.items = items
        self.max_weight = max_weight

    def _evaluate_individual(self, individual):
        """
        Compute the fitness value of a given individual.

        Parameters
        ----------
        individual: Vector
            The individual to compute the fitness value for.

        Returns
        -------
        float
            The evaluated fitness value of the given individual.
        """
        weight, value = 0.0, 0.0
        for i in range(individual.size()):
            if individual.cell_value(i):
                weight += self.items[i][0]
                value += self.items[i][1]

        # worse possible fitness is returned if the weight of the items exceeds the maximum weight of the bag
        if weight > self.max_weight:
            return -np.inf

        # fitness value is the total value of the bag
        return value