from __future__ import annotations
from abc import ABC, abstractmethod


class ICommand(ABC):
    """
    Interface para as classes de comando.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class LightOnCommand(ICommand):
    """
    Comando responsável por executar o método light_on implementado no Receiver.
    """

    def __init__(self, receiver: Receiver, place: str) -> None:
        self._receiver = receiver
        self._place = place

    def execute(self) -> None:
        """
        Responsável por executar o método Receiver referente a acender as luzes de um ambiente.
        """
        print("\nLightOnCommand: Em execução...", end="")
        self._receiver.light_on(self._place)


class ChangeColorCommand(ICommand):
    """
    Comando responsável por executar o método change_color implementado no Receiver.
    """

    def __init__(self, receiver: Receiver, color: str) -> None:
        self._receiver = receiver
        self._color = color

    def execute(self) -> None:
        """
        Responsável por executar o método Receiver referente a mudança de cor da iluminação.
        """

        print("\nChangeColorCommand: Em execução...", end="")
        self._receiver.change_color(self._color)


class Receiver:
    """
    O Receiver é responsável por implementar a lógica de negócio,
    executando as operações pertinentes aos comandos implementados.
    """

    def light_on(self, place: str) -> None:
        print(
            f"\nReceiver: Ligando a iluminação do ambiente -> {place}.", end="")

    def change_color(self, color: str) -> None:
        print(
            f"\nReceiver: Alterando a cor da iluminação para -> {color}.", end="")


class Invoker:
    """
    Responsável por fazer a associação dos comandos e mandar uma requisição de execução.
    """

    _on_start = None
    _on_finish = None

    def set_on_start(self, command: ICommand):
        """Atribui a instância passada para a váriavel _on_start."""
        self._on_start = command

    def set_on_finish(self, command: ICommand):
        """Atribui a instância passada para a váriavel _on_finish."""
        self._on_finish = command

    def invoke_command(self) -> None:
        """
        Valida se existe uma instância de ICommand atrelada as váriaveis on_start e on_finish. \n
        True: Aciona o método execute. \n
        False: Não executa nada.
        """

        if isinstance(self._on_start, ICommand):
            self._on_start.execute()

        if isinstance(self._on_finish, ICommand):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    Client responsável por acionar a classe Invoker.
    """

    invoker = Invoker()
    receiver = Receiver()

    invoker.set_on_start(LightOnCommand(receiver, "Sala"))
    invoker.set_on_finish(ChangeColorCommand(
        receiver, "Azul"))

    invoker.invoke_command()
