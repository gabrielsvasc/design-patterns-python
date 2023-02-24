"""
O Decorator é um padrão estrutural que permite adicionar novos comportamentos
aos objetos dinamicamente, colocando-os dentro de objetos wrapper especiais.

Identificação: O Decorator pode ser reconhecido por métodos de criação ou
construtores que aceitam objetos da mesma classe ou interface que uma
classe atual.
"""


class IComponent():
    """
    A interface do Component define a operação que pode ser alterada pelo
    Decorator.
    """

    def operation(self) -> str:
        pass


class Component(IComponent):
    """
    O Component implementa o método operation, que será utilizado pelo decorator.
    """

    def operation(self) -> str:
        return "Component"


class IDecorator(IComponent):
    """
    O IDecorator herda da mesma interface do Component. Seu propósito é definir
    o encapsulamento que será aplicado pelos decoradores concretos.
    """

    _component: IComponent = None

    def __init__(self, component: IComponent) -> None:
        self._component = component

    @property
    def component(self) -> IComponent:
        """
        O Decorator delega o trabalinho para o component encapsulado.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class DecoratorUp(IDecorator):
    """
    O decorador concreto chama o componente encapsulado e alterando o
    seu resultado de alguma forma.
    """

    def operation(self) -> str:
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.

        Aqui o Decorator chama a operação do Component recebido para obter seu valor.
        Neste exemplo o decorador vai tornar as letras do valor recebido em maiúsculas.
        """
        operation = self.component.operation()

        return f"Decorator({operation.upper()})"


class DecoratorLow(IDecorator):
    """
    O Decorator pode aplicar sua ação antes ou depois da chamado do objeto encapsulado.
    """

    def operation(self) -> str:
        """
        Neste exemplo o decorador vai tornar as letras do valor recebido em minúsculas.
        """
        operation = self.component.operation()

        return f"Decorator({operation.lower()})"


def client_code(component: IComponent) -> None:
    """
    O Client vai atuar com qualquer classe que implemente a interface IComponent.
    """
    print(f"Result: {component.operation()}")


if __name__ == "__main__":
    print("Client: sem decorador...")
    simple = Component()
    client_code(simple)
    print("\n")

    print("Client: com decorador de texto em caixa alta...")
    decorator1 = DecoratorUp(simple)
    client_code(decorator1)
    print("\n")

    decorator2 = DecoratorLow(decorator1)
    print("Client: com decorador de texto em caixa baixa...")
    client_code(decorator2)
