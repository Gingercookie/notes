import math
class Tire:
    """
    Tire represents a tire that could be used on a car.
    """

    def __init__(self, width, ratio, diameter, brand='Michelin', standard='P'):
        self.standard = standard
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand

    def circumference(self):
        """
        The circumference of the tire in inches.

        >>> tire = Tire(205, 65, 15)
        >>> tire.circumference()
        80.1
        """

        total_diameter = self._side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)


    def __repr__(self):
        """
        Represent the tire's information in the standard notion
        on the side of the tire. Example: 'Michelin tire: P215/65R15'
        """

        return (f"{self.brand} tire: "
            + f"{self.standard}{self.width}/{self.ratio} R{self.diameter}")

    def _side_wall_inches(self):
        return (self.width * (self.ratio / 100)) / 25.4


class SnowTire(Tire):
    def __init__(self, width, ratio, diameter, chain_thickness, brand='Michelin', standard='P'):
        super().__init__(width, ratio, diameter, brand, standard)
        self.chain_thickness = chain_thickness

    def circumference(self):
        """
        The circumference of a tire with snow chains, in inches.

        >>> tire = SnowTire(205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """

        total_diameter = (self._side_wall_inches() + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        return super().__repr__() + " (Snow)"
