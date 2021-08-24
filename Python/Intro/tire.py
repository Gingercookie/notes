import math
class Tire:
    """
    Tire represents a tire that could be used on a car.
    """

    def __init__(self, width, ratio, diameter, brand='Michelin', speed_rating='H', standard='P', tire_type='all-weather'):
        self.standard = standard
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.speed_rating = speed_rating
        self.tire_type = tire_type

    def circumference(self):
        """
        The circumference of the tire in inches.

        >>> tire = Tire(205, 65, 15)
        >>> tire.circumference()
        80.1
        """

        side_wall_inches = (self.width * (self.ratio / 100)) / 25.4
        total_diameter = side_wall_inches * 2 + self.diameter
        return round(total_diameter * math.pi, 1)


    def __repr__(self):
        """
        Represent the tire's information in the standard notion
        on the side of the tire. Example: 'Michelin snow tire: P215/65R15'
        """

        return (f"{self.brand} {self.tire_type} tire: "
            + f"{self.standard}{self.width}/{self.ratio}"
            + f"R{self.diameter} {self.speed_rating}")
