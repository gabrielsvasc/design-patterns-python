from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class IHandler(ABC):
    """
    Interface para definição dos métodos do handler.
    """

    @abstractmethod
    def set_next(self, handler: IHandler) -> IHandler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(IHandler):
    """
    Classe abstrata com implementação default dos métodos.
    """
    _next_handler: IHandler = None

    def set_next(self, handler: IHandler) -> IHandler:
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class MonkeyHandler(AbstractHandler):
    """
    Primeiro método na cadeia de execução.
    """

    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"MONKEY: Vou comer a {request}!"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    """
    Segundo método na cadeia de execução.
    """

    def handle(self, request: Any) -> str:
        if request == "Noz":
            return f"SQUIRREL: Quebrando a {request}..."
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    """
    Terceiro método na cadeia de execução.
    """

    def handle(self, request: Any) -> str:
        if request == "Osso":
            return f"DOG: Roendo {request}..."
        else:
            return super().handle(request)


def client_code(handler: IHandler, request: str) -> None:
    """
    Client recebe o Handler e executa a requisição.
    """
    result = handler.handle(request)

    if result:
        print(result)
    else:
        print(f"HANDLER: Requisição não atendida.")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # Monkey
    client_code(monkey, 'Banana')
    # Monkey > Squirrel
    client_code(monkey, 'Noz')
    # Monkey > Squirrel > Dog
    client_code(monkey, 'Osso')
    # Monkey > Squirrel > Dog > Default
    client_code(monkey, 'Carne')
