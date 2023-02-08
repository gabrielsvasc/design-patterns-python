"""
  O Memento é um padrão de projeto comportamental que permite tirar
  um “retrato” do estado de um objeto e restaurá-lo no futuro.

  Aplicação: O padrão Memento é utilizado para produzir retratos do estado
  de um objeto para ser capaz de restaurar um estado anterior do objeto.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class IMemento(ABC):
    """
    Interface do Memento que define os métodos que devolvem
    informações.

    Ex: (nome, data e estado).
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass


class Memento(IMemento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        Utilizado pelo Originator para restaurar seu estado.
        """
        return self._state

    def get_name(self) -> str:
        """
        Utilizado pelo Caretaker para retornar o nome.
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        """
         Utilizado pelo Caretaker para retornar a data.
        """
        return self._date


class Originator():
    """
    Classe principal que terá o Memento para controle de estado.
    """

    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: estado inicial {self._state}")

    def do_something(self) -> None:
        """
        Este método simula a lógica de negócio que altera o estado do objeto.
        """

        self._state = self._generate_random_string(30)
        print(f"Originator: estado alterado para {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self) -> IMemento:
        """
        Armazena o estado atual dentro de um Memento.
        """

        return Memento(self._state)

    def restore(self, memento: IMemento) -> None:
        """
        Retorna ao estado anterior utilizando o Memento.
        """

        self._state = memento.get_state()
        print(f"Originator: Estado restaurado para {self._state}")


class Caretaker():
    """
    Está classe apenas intermédia as operações entre o Memento
    e o Originator, sendo assim, não possui nenhum conhecimento sobre
    o estado.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Salvando estado do Originator...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restaurando estado para {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Histórico do Memento")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.show_history()

    caretaker.undo()

    caretaker.undo()
