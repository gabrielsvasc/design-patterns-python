"""
    O Singleton é um padrão de projeto criacional, que garante que
    apenas um objeto desse tipo exista e forneça um único ponto de
    acesso a ele para qualquer outro código.

    Identificação: O Singleton pode ser reconhecido por um método
    de criação estático, que retorna o mesmo objeto em cache.
"""

from __future__ import annotations


class SingletonMeta(type):
    """
    Metaclass usada para implementação do Singleton.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Valida se já existe uma instância da classe,
        se não armazena os valores da mesma no dict instances.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def memory_value(self) -> Singleton:
        return self


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Sucesso, ambos possuem a mesma instância.")
        print(f'S1: {s1.memory_value()}')
        print(f'S2: {s2.memory_value()}')

    else:
        print("Falha, as variáveis possuem instâncias diferentes.")
