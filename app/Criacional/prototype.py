"""
    Todas as classes de prototypes(protótipos) devem ter uma interface
    comum que permita copiar objetos, mesmo que suas classes concretas
    sejam desconhecidas. Objetos protótipos podem produzir cópias completas,
    pois objetos da mesma classe podem acessar os campos privados um do outro.

    Identificação: O prototype pode ser facilmente reconhecido pelos
    métodos clone ou copy, etc.
"""
from __future__ import annotations
from copy import deepcopy


class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addres: list[Address] = []

    def add_address(self, address: str) -> None:
        self.addres.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address:
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":
    # Person 1 com Nome: Gabriel  Sobrenome: Vasconcelos
    person1 = Person('Gabriel', 'Vasconcelos')
    address = Address('Rua Teste', '123')
    person1.add_address(address)

    # Clonando o Person 1 COM Protoype
    person2 = person1.clone()
    person2.firstname = 'Leirbag'
    person2.lastname = 'Vasc'

    # Clonando o Person 1 SEM Protoype
    person3 = person1
    person3.firstname = 'Oswaldo'
    person3.lastname = 'Cruz'

    print(
        f'Nome: {person1.firstname} - Sobrenome: {person1.lastname}')
    print(
        f'Nome: {person2.firstname} - Sobrenome: {person2.lastname}')
    print(
        f'Nome: {person3.firstname} - Sobrenome: {person3.lastname}')
