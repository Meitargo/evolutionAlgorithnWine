"""
This module implements the vector class.
"""

from random import randint

from eckity.genetic_encodings.ga.vector_individual import Vector


class BitStringVector(Vector):
    def __init__(self,
                 fitness,
                 length,
                 bounds=(0, 1)):
        super().__init__(fitness, length, bounds)

    def get_random_number_in_bounds(self, index):
        # todo check if need to check bounds - is it tuple always?
        return randint(self.bounds[0], self.bounds[1])

# end class bit string vector