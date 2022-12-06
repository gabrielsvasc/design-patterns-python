from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    """Classe que abstrai metodo."""
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    """Classe que implementa metodo da Veiculo."""

    def buscar_cliente(self) -> None:
        print("Carro de luxo indo até o cliente")


class CarroPopular(Veiculo):
    """Classe que implementa metodo da Veiculo."""

    def buscar_cliente(self) -> None:
        print("Carro popular indo até o cliente")


class Moto(Veiculo):
    """Classe que implementa metodo da Veiculo."""

    def buscar_cliente(self) -> None:
        print("Moto indo até o cliente")


class VeiculoFactory(ABC):
    """Classe abstrata que gera classes concretas."""

    def __init__(self, tipo: str) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        else:
            raise ValueError("Veiculo não existe.")

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    """Classe concreta de VeiculoFactory usada na Service."""
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        else:
            raise ValueError("Veiculo não existe.")


if __name__ == "__main__":
    """Service que utiliza o metodo criado."""
    carros_disponiveis_ZN = ['popular', 'moto']

    for i in range(10):
        tipo_carro = choice(carros_disponiveis_ZN)
        carro = ZonaNorteVeiculoFactory(tipo_carro)
        carro.buscar_cliente()
