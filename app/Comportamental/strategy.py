"""
    O Strategy é um padrão de projeto comportamental que transforma
    um conjunto de comportamentos em objetos e os torna intercambiáveis
    dentro do objeto de contexto original.

    Identificação: O padrão Strategy pode ser reconhecido por um método que
    permite que o objeto aninhado faça o trabalho real, bem como pelo setter
    que permite substituir esse objeto por outro diferente.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Ordenator():
    """Contexto que define a Strategy e aplica a mesma conforme necessário."""

    def __init__(self, data: List, strategy: IOrder) -> None:
        self._strategy = strategy
        self.data = data

    @property
    def strategy(self) -> IOrder:
        """Getter da Strategy."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: IOrder) -> None:
        """Setter da Strategy."""
        self._strategy = strategy

    def order_by(self) -> None:
        """O Context utiliza a ordenação definida na Strategy."""
        result = self._strategy.order(self.data)
        print(",".join(result))


class IOrder(ABC):
    """Interface para implementação da Strategy."""
    @abstractmethod
    def order(self, data: List):
        pass


class OrderAsc(IOrder):
    """Implementação da Strategy de ordenação ascendente."""

    def order(self, data: List) -> List:
        return sorted(data)


class OrderDesc(IOrder):
    """Implementação da Strategy de ordenação descendente."""

    def order(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":

    lstLetters = ['a', 'b', 'c', 'd', 'e']

    context = Ordenator(lstLetters, OrderAsc())
    print("Client: Utilizando Strategy Ascendente.")
    context.order_by()
    print()

    print("Client: Utilizando Strategy Descendente.")
    context.strategy = OrderDesc()
    context.order_by()
