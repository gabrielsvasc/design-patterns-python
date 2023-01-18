"""
    Diferente de outros padrões de criação, o Builder não exige que os
    produtos tenham uma interface comum. Isso torna possível produzir
    produtos diferentes usando o mesmo processo de construção.

    Identificação: O padrão Builder pode ser reconhecido na classe que possui
    um único método de criação e vários métodos para configurar o objeto resultante.
    Os métodos do Builder geralmente suportam encadeamento.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class ICarBuilder(ABC):
    """Interface do Car."""
    @property
    @abstractmethod
    def result(self) -> Car: pass

    @abstractmethod
    def reset(self) -> None: pass

    @abstractmethod
    def set_seats(self) -> None: pass

    @abstractmethod
    def set_engine(self) -> None: pass

    @abstractmethod
    def set_turbo(self) -> Car: pass

    @abstractmethod
    def set_sunroof(self) -> Car: pass


class CarBuilder(ICarBuilder):
    """Concrete Builder do Car."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    @property
    def result(self) -> Car:
        car = self._car
        self.reset()
        return car

    def set_seats(self, seats: int) -> None:
        self._car.add(('seats', seats))

    def set_engine(self, engine_type: str) -> None:
        self._car.add(('engine', engine_type))

    def set_sunroof(self) -> None:
        self._car.add(('sunroof', True))

    def set_turbo(self) -> None:
        self._car.add(('turbo', True))


class Car:
    """Produto Car construido pelo Builder."""

    def __init__(self) -> None:
        self.parts: list[tuple] = []

    def add(self, part: tuple) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        for part in self.parts:
            print(part)


class CarDirector:
    """Responsável por controlar a criação de objetos do tipo Car."""

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> CarBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: CarBuilder) -> None:
        self._builder = builder

    def builder_popular_car(self) -> None:
        self.builder.set_seats(4)
        self.builder.set_engine('manual')

    def builder_sport_car(self) -> None:
        self.builder.set_seats(2)
        self.builder.set_engine('auto')
        self.builder.set_sunroof()
        self.builder.set_turbo()


if __name__ == "__main__":
    """Client."""
    director = CarDirector()
    builder = CarBuilder()
    director.builder = builder

    print("Carro popular: ")
    director.builder_popular_car()
    builder.result.list_parts()

    print("\n")

    print("Carro esportivo: ")
    director.builder_sport_car()
    builder.result.list_parts()
