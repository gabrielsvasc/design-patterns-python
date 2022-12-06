from __future__ import annotations
from abc import ABC, abstractmethod


class VeiculoAbstract(ABC):
    """Abstract Factory - interface que declara um conjunto de métodos
    que retornam diferentes produtos abstratos."""
    @abstractmethod
    def create_carro(self) -> CarroAbstract: pass

    @abstractmethod
    def create_moto(self) -> MotoAbstract: pass


class VeiculoConcrete(VeiculoAbstract):
    """Concrete Factory - cria os objetos pertencentes
    a Factory de veiculos.
    ."""

    def create_carro(self) -> CarroAbstract:
        return CarroConcrete()

    def create_moto(self) -> MotoAbstract:
        return MotoConcrete()


class CarroAbstract(ABC):
    """Interface base para os Carros da Factory."""
    @abstractmethod
    def buscar_cliente(self, endereco_partida: str,
                       endereco_destino: str) -> dict: pass


class MotoAbstract(ABC):
    """Interface base para as Motos da Factory."""
    @abstractmethod
    def buscar_encomenda(self, endereco_partida: str,
                         endereco_destino: str) -> dict: pass

    @abstractmethod
    def pegar_assinatura(self, nome: str) -> str: pass


class CarroConcrete(CarroAbstract):
    """Implementação concreta do objeto Carro."""

    def buscar_cliente(self, endereco_partida: str, endereco_destino: str) -> dict:
        return {
            'partida': endereco_partida,
            'destino': endereco_destino,
        }


class MotoConcrete(MotoAbstract):
    """Implementação concreta do objeto Moto."""

    def buscar_encomenda(self, endereco_partida: str, endereco_destino: str) -> dict:
        return {
            'partida': endereco_partida,
            'destino': endereco_destino,
        }

    def pegar_assinatura(self, nome: str) -> str:
        return nome


# Exemplo de cliente fazendo uso da Abstract Factory
def client_code(factory: VeiculoAbstract) -> None:
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
    client = client_code(VeiculoConcrete())
