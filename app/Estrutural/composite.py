"""
O Composite é um padrão de projeto estrutural que permite compor objetos
em uma estrutura semelhante a uma árvore e trabalhar com eles como se
fosse um objeto singular.

Identificação: É fácil reconhecer o Composite por métodos comportamentais,
levando uma instância do mesmo tipo abstrato/interface para uma estrutura
em árvore.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IComponent(ABC):
    """
    A interface do Component declara operações comuns entre o Leaf e o
    Composite.
    """

    @property
    def parent(self) -> IComponent:
        return self._parent

    @parent.setter
    def parent(self, parent: IComponent):
        """
        O Component pode declarar o GET e o SET para o atríbuto parents,
        garantindo o acesso do mesmo na estrutura de árvore, além de
        permitir uma forma padão para setar os valores do mesmo.
        """

        self._parent = parent

    """
    Para algumas situações será interessante definir o controle das
    operações diretamente pelo Component. Dessa forma, torna-se mais
    fácil a montagem da estrutura dos objetos. Um ponto negativo é que
    esses métodos não terão nenhuma instanciação na classe Leaf.
    """

    def add(self, component: IComponent) -> None:
        pass

    def remove(self, component: IComponent) -> None:
        pass

    def is_composite(self) -> bool:

        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(IComponent):
    """
    O Leaf representa o ponto final da composição, está classe não pode ter
    outros filhos.

    Geralmente será nesse ponto que as ações serão executadas efetivamente,
    enquanto o Composite apenas distribui o trabalho para as sub-classes.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(IComponent):
    """
    O Composite reprenta a parte completa da estrutura, que geralmente
    possui filhos. Está classe delega os serviços para o Leaf e após
    isso resume o resultado.
    """

    def __init__(self) -> None:
        self._children: List[IComponent] = []

    """
    O Composite pode adicionar ou remover outros componentes, sejam eles
    simples ou complexos.
    """

    def add(self, component: IComponent) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: IComponent) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        Aqui o Composite executa as operações dos objetos, caminhando de
        forma recursiva por todos os filhos, coletando e agregando seus
        resultados.
        """

        results = []

        for child in self._children:
            results.append(child.operation())

        return f"Branch({'+'.join(results)})"


def client_code(component: IComponent) -> None:
    """
    O Client atua com todos os componentes através da interface.
    """

    print(f"Result: {component.operation()}", end="")


def client_code2(component1: IComponent, component2: IComponent) -> None:
    """
    Graças ao fato das operações de ambos os objetos (simples e complexos),
    serem declaradas na Interface base, o Client consegue atuar com
    qualquer componente, sem nenhuma dependências com a classe concreta.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"Result: {component1.operation()}", end="")


if __name__ == "__main__":
    simple = Leaf()
    print("Client: utilizando apenas um compontente simples...")
    client_code(simple)
    print("\n")

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: utilizando árvore de composição...")
    client_code(tree)
    print("\n")

    print("Client: controlando árvore de composição...")
    client_code2(tree, simple)
