"""
    O Singleton é um padrão de projeto criacional, que garante que
    apenas um objeto desse tipo exista e forneça um único ponto de
    acesso a ele para qualquer outro código.

    Identificação: O Singleton pode ser reconhecido por um método
    de criação estático, que retorna o mesmo objeto em cache.
"""


from __future__ import annotations
from threading import Lock, Thread


class SingletonMeta(type):
    """
    Metaclass usada para implementação do Singleton com multi-thread.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    Metodo de trava para assegurar
    a mesma instância em todas as threads.
    """

    def __call__(cls, *args, **kwargs):
        """
        Trava a execução das demais threads e valida se já existe uma instância
        da classe, se não armazena os valores da mesma no dict instances.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def memory_value(self) -> Singleton:
        return self


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(f'VALUE: {singleton.value} | MEMORY: {singleton.memory_value()}')


if __name__ == "__main__":

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
