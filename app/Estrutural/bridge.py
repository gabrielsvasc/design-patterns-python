"""
O Bridge é um padrão de projeto estrutural que divide a lógica de negócio ou uma  enorme
classe em hierarquias de classe separadas que podem ser desenvolvidas independentemente.

Identificação: O Bridge pode ser reconhecida por uma distinção clara entre alguma entidade
controladora e várias plataformas diferentes nas quais ela se baseia.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """
    A Abstraction define os métodos que vão interagir com a Implementation,
    para que isso seja possível iremos delegar todas as operações para o
    objeto definido na inicialização.
    """

    def __init__(self, implementation: Implementation) -> None:
        self._implementation = implementation
        self._name = self.__class__.__name__

    def toggle_power(self) -> None:
        if (self._implementation._power):
            self._implementation.disable()
        else:
            self._implementation.enable()

    def volume_down(self) -> None:
        volume = self._implementation._volume - 10
        self._implementation.set_volume(volume)

    def volume_up(self) -> None:
        volume = self._implementation._volume + 10
        self._implementation.set_volume(volume)


class ExtendedAbstraction(Abstraction):
    """
    Estende a Abstraction sem alterar suas implementações.
    """

    def mute(self):
        self._implementation.set_volume(0)


class Implementation(ABC):
    """
    Interface padrão para todas as classes que serão implementadas.
    Geralmente proporciona operações mais primitivas, deixando que a Abstraction
    as aperfeiçoe conforme necessário.
    """

    _volume: int
    _power: bool

    @abstractmethod
    def enable() -> None:
        pass

    @abstractmethod
    def disable() -> None:
        pass

    @abstractmethod
    def set_volume() -> None:
        pass


class TVImplementation(Implementation):
    def __init__(self):
        self._volume = 30
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if ((self._volume < 100) and (self._volume > 0) and (self._power is not False)):
            self._volume = volume

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        if (power != self._power):
            self._power = power

    def enable(self) -> None:
        self.power = True
        print(f"Implementation: [{self._name}] ligado")

    def disable(self) -> None:
        self.power = False
        print(f"Implementation: [{self._name}] desligado")

    def set_volume(self, volume: int) -> None:
        self.volume = volume
        print(f"Implementation: [{self._name}] volume {self._volume}")


class RadioImplementation(TVImplementation):
    # Herda as implementações da TVImplementation
    ...


def client_code(abstraction: Abstraction | ExtendedAbstraction) -> None:
    """
    O Client executa os métodos da Implementation através da Abstraction,
    podendo também fazer uso de qualquer classe que estenda a mesma.
    """

    abstraction.toggle_power()
    abstraction.volume_down()
    abstraction.volume_up() if abstraction._name == 'Abstraction' else abstraction.mute()
    abstraction.toggle_power()


if __name__ == "__main__":
    implementation = TVImplementation()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = RadioImplementation()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
