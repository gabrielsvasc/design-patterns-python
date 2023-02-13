""""
O Visitor é um padrão de projeto comportamental que permite adicionar
novos comportamentos à hierarquia de classes existente sem alterar
nenhum código existente.

Identificação: O padrão Visitor é utilizado nas situações em que se
deseja executar operações sobre diversos elementos que dependem apenas
das suas classes concretas, não possuindo uma interface comum.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IComponent(ABC):
    """
    Interface do componente que abstrai o método accept,
    tornando obrigatório que um Visitor seja passado.
    """

    @abstractmethod
    def accept(self, visitor: IVisitor) -> None:
        pass


class IVisitor(ABC):
    """
    Interface do Visitor, responsável por definir os métodos abstratos
    que visitam cada um dos componentes, tornando obrigatório que cada
    Component seja passado para o Visitor.
    """

    @abstractmethod
    def visit_component_a(self, element: ComponentA) -> None:
        pass

    @abstractmethod
    def visit_component_b(self, element: ComponentB) -> None:
        pass


class ComponentA(IComponent):
    def increase_order(self, order_amount: int):
        return order_amount + 5

    def accept(self, visitor: IVisitor) -> None:
        visitor.visit_component_a(self)


class ComponentB(IComponent):
    def take_order(self, amount_received: int, transporter: str) -> int:
        order = self.amount_taken(amount_received, transporter)
        return order

    def amount_taken(self, amount_received: int, transporter: str) -> int:
        if transporter == 'SEDEX':
            return amount_received - 1
        else:
            return amount_received

    def accept(self, visitor: IVisitor) -> None:
        visitor.visit_component_b(self)


class VisitorA(IVisitor):
    def visit_component_a(self, element: ComponentA) -> None:
        print(f"VisitorA: valor retornado {element.increase_order(5)}.")

    def visit_component_b(self, element: ComponentB) -> None:
        print(f"VisitorA: valor retornado {element.take_order(5, 'SEDEX')}.")


class VisitorB(IVisitor):
    def visit_component_a(self, element: ComponentA) -> None:
        print(
            f"VisitorB: valor retornado {element.increase_order(4)}.")

    def visit_component_b(self, element: ComponentB) -> None:
        print(
            f"VisitorB: valor retornado {element.amount_taken(2, 'OTHER')}.")


def client_code(components: List[IComponent], visitor: IVisitor) -> None:
    """
    Código do client responsável por executar o fluxo do Visitor.
    """

    for component in components:
        component.accept(visitor)


if __name__ == "__main__":
    components = [ComponentA(), ComponentB()]

    visitor1 = VisitorA()
    client_code(components, visitor1)

    visitor2 = VisitorB()
    client_code(components, visitor2)
