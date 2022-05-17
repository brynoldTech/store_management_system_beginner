from abc import ABC, abstractmethod

""" lets make this class as abstract class """


class Government(ABC):
    """lets make this method as abstract method """

    @abstractmethod
    def add_product(self):
        """ this implementation are in the sub class called SuperMarket"""
        pass

    @abstractmethod
    def view_product(self):
        """ this implementation are in the sub class called SuperMarket"""
        pass

    @abstractmethod
    def remove_product(self):
        """ this implementation are in the sub class called SuperMarket"""
        pass
