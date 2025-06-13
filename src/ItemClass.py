"""
Outline for an inventory item class

Author: Garret Wilson
Last updated: 08/06/2024
"""


class Item:
    """
    An instance of this class describes an inventory item

    Attributes:
        _name: the name of the inventory item
        _count: batch size measured
        _mass: batch size mass

    Methods:
        get_name: retrieves the name of the inventory item
        get_count: retrieves the batch size of the inventory item
        get_mass: retrieves the mass of the batch size

        calculate_total_count_v1: takes one input, the total weight of all the inventory
            items (in ounces), and calculates an estimate of the total number of inventory
            items

        calculate_total_count_v2: takes two inputs, the total weight of some inventory items
            (in ounces) and the current count of inventory items, and calculates an estimate
            of the total number of inventory items
    """

    def __init__(self, name, count, mass):
        self._name = name
        self._count = count
        self._mass = mass

    def get_name(self):
        return self._name

    def get_count(self):
        return self._count

    def get_mass(self):
        return self._mass

    def calculate_total_count_v1(self, total_mass):
        temp = float(total_mass / self._mass)
        return round(float(temp * self._count), 2)

    def calculate_total_count_v2(self, total_mass, count_value):
        temp = float(total_mass / self._mass)
        return round(float(temp * self._count) + count_value, 2)
