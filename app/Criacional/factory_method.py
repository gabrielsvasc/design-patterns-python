"""
O Factory Method define um método, que deve ser usado para criar
objetos em vez da chamada direta ao construtor. As subclasses podem
substituir esse método para alterar a classe de objetos que serão criados.

Identificação: Os métodos fábrica podem ser reconhecidos por
métodos de criação, que criam objetos de classes concretas,
mas os retornam como objetos de tipo ou interface abstrata.
"""


from __future__ import annotations
from abc import ABC, abstractmethod


class IFactory(ABC):
    """
    Interface para implementação da Factory.
    """

    @abstractmethod
    def factory_method(self):
        """
        Implementação padrão do Factory Method.
        """
        pass

    def transporting_product(self) -> str:
        """
        Lógica de negócio associada ao produto criado.
        """

        # Call the factory method to create a Product object.
        vehicle: IVehicle = self.factory_method()

        # Now, use the product.
        result = f"{vehicle.take_product()}"

        return result


class CarFactory(IFactory):
    """
    Implementação concreta da Factory.
    """

    def factory_method(self) -> IVehicle:
        return Car()


class MotorcycleFactory(IFactory):
    """
    Implementação concreta da Factory.
    """

    def factory_method(self) -> IVehicle:
        return Motorcycle()


class IVehicle(ABC):
    """
    Interface do produto a ser criado na Factory.
    """

    @abstractmethod
    def take_product(self) -> str:
        pass


class Car(IVehicle):
    """
    Implementação concreta do produto.
    """

    def take_product(self) -> str:
        return "Transporting product with car."


class Motorcycle(IVehicle):
    """
    Implementação concreta do produto.
    """

    def take_product(self) -> str:
        return "Transporting product with motorcycle."


if __name__ == "__main__":
    car = CarFactory()
    moto = MotorcycleFactory()

    print(car.transporting_product())
    print(moto.transporting_product())
