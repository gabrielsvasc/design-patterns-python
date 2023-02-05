"""
    O Mediator é um padrão de projeto comportamental que reduz o
    acoplamento entre os componentes de um programa, fazendo-os se
    comunicar indiretamente, por meio de um objeto mediador especial.

    Identificação: O uso mais popular do padrão Mediator no código Python
    é facilitar a comunicação entre os componentes de interface do usuário
    de uma aplicação. O sinônimo do Mediator é a parte do Controlador do
    padrão MVC.
"""
from __future__ import annotations
from abc import ABC


class IMediator(ABC):
    """
    Interface utilizada na classe mediadora, que implementa um método
    notify.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(IMediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            self._component2.do_c()
        elif event == "D":
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    Componente base responsável por associar um mediador.
    """

    def __init__(self, mediator: IMediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> IMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: IMediator) -> None:
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component1: Fazendo A...")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component1: Fazendo B...")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component2: Fazendo C...")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component2: Fazendo D...")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    # do_a > notify > do_c
    c1.do_a()

    # do_d > notify > do_b > do_b
    c2.do_d()
