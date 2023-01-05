from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IObservable(ABC):
    """Interface para implementação do Observable."""

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        """Vincula um Observer ao Observable."""
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        """Desvincula um Observer do Observable."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notifica todos os Observers sobre o evento."""
        pass


class Product(IObservable):
    """Implementação dos metodos do Observable."""

    _state: int = None

    _observers: List[IObserver] = []

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def product_available(self) -> None:
        """Altera o State do produto para disponível (1) e notifica os Observers."""
        self._state = 1

        self.notify()


class IObserver(ABC):
    """Interface com o metodo Update utilizado pelo Observable."""

    @abstractmethod
    def update(self, subject: IObservable) -> None:
        """Recebe a atualização do Observable."""
        pass


class ClientA(IObserver):
    def update(self, subject: IObservable) -> None:
        if subject._state == 1:
            print("ClientA: indo comprar o produto...")


class ClientB(IObserver):
    def update(self, subject: IObservable) -> None:
        if subject._state == 1:
            print("ClientB: indo comprar o produto em 1H...")


if __name__ == "__main__":

    subject = Product()

    observer_a = ClientA()
    subject.add_observer(observer_a)

    observer_b = ClientB()
    subject.add_observer(observer_b)

    subject.product_available()
    subject.product_available()

    subject.remove_observer(observer_a)

    subject.product_available()
