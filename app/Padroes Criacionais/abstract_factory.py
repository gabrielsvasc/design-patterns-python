from __future__ import annotations
from abc import ABC, abstractmethod


class IVehicle(ABC):
    """
    Interface com metodos que devem ser
    implementados na classe Vehicle.
    """

    @abstractmethod
    def create_carro(self) -> ICar: pass

    @abstractmethod
    def create_moto(self) -> IMotorcycle: pass


class Vehicle(IVehicle):
    """
    Implementa os metodos da Interface Vehicle.
    """

    def create_carro(self) -> ICar:
        return Car()

    def create_moto(self) -> IMotorcycle:
        return Motorcycle()


class ICar(ABC):
    """
    Interface com metodos que devem ser
    implementados na classe Car.
    """

    @abstractmethod
    def buscar_cliente(self, endereco_partida: str,
                       endereco_destino: str) -> dict: pass


class IMotorcycle(ABC):
    """
    Interface com metodos que devem ser
    implementados na classe Motorcycle.
    """

    @abstractmethod
    def buscar_encomenda(self, endereco_partida: str,
                         endereco_destino: str) -> dict: pass

    @abstractmethod
    def pegar_assinatura(self, nome: str) -> str: pass


class Car(ICar):
    """
    Implementa os metodos da Interface Car.
    """

    def buscar_cliente(self, endereco_partida: str, endereco_destino: str) -> dict:
        return {
            'partida': endereco_partida,
            'destino': endereco_destino,
        }


class Motorcycle(IMotorcycle):
    """
    Implementa os metodos da Interface Motorcycle.
    """

    def buscar_encomenda(self, endereco_partida: str, endereco_destino: str) -> dict:
        return {
            'partida': endereco_partida,
            'destino': endereco_destino,
        }

    def pegar_assinatura(self, nome: str) -> str:
        return nome


# Exemplo de cliente fazendo uso da Abstract Factory
def client_code(factory: IVehicle) -> None:
    carro = factory.create_carro()
    moto = factory.create_moto()

    print(f"""Carro:
        {carro.buscar_cliente('R. Teste 123', 'Rua Destino 321')}
          """)

    print("\n")

    print(f"""Moto:
        {moto.buscar_encomenda('R. Teste 123', 'Rua Destino 321')}
        Assinatura: {moto.pegar_assinatura('Gabriel')}
    """)


if __name__ == "__main__":
    client = client_code(Vehicle())
