from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo indo até o cliente")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular indo até o cliente")


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto indo até o cliente")


class VeiculoFactory:
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


if __name__ == "__main__":
    carros_disponiveis = ['luxo', 'popular', 'moto']

    for i in range(10):
        tipo_carro = choice(carros_disponiveis)
        carro = VeiculoFactory(tipo_carro)
        carro.buscar_cliente()
