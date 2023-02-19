"""
    O Flyweight é um padrão de projeto estrutural que permite que os
    programas suportem grandes quantidades de objetos, mantendo baixo o
    consumo de memória.

    Identificação: O Flyweight pode ser reconhecido por um método de criação
    que retorna objetos em cache em vez de criar novos.
"""
import json
from typing import Dict, List


class Flyweight():
    """
    O Flyweight armazena o estado intrínseco de uma entidade, compartilhando o
    mesmo para evitar objetos duplicados. Além disso, é possível receber o
    estado Extrínsico único para cada objeto através dos seus métodos.
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        _state = json.dumps(self._shared_state)
        _unique_state = json.dumps(unique_state)
        print(
            f"Flyweight: Intrínseco ({_state}) | Extrínsico ({_unique_state}).", end="")


class FlyweightFactory():
    """
    O FlyweightFactory cria e controla os objetos Flyweight. Garantindo o
    devido compartilhamento, além de controlar os acessos do Client, validando
    se o mesmo já existe, criando um novo objeto caso contrário.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: List) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: List) -> str:
        """
        Concatena os valores da lista e retorna como string.
        """

        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: List) -> Flyweight:
        """
        Busca pelo Flyweight recebido, se este já existir apenas o retorna,
        caso contrário, cria um novo com os valores passados.
        """

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: não localizado, criando um novo...")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Localizado, retornando o mesmo.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: {count} flyweights encontrados:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory,
    plates: str,
    owner: str,
    brand: str,
    model: str,
    color: str
) -> None:
    print("\n\nClient: Adicionando carro a base de dados.")
    flyweight = factory.get_flyweight([brand, model, color])

    flyweight.operation([plates, owner])


if __name__ == "__main__":
    """
    Simula o Client Code que interage e popula o Flyweight com dados.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()
