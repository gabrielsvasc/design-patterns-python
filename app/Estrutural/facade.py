"""
  O Facade é um padrão de projeto estrutural que fornece uma interface
  simplificada (mas limitada) para um sistema complexo de classes,
  biblioteca, ou framework.

  Identificação: O Facade pode ser reconhecido em uma classe que possui uma
  interface simples, mas delega a maior parte do trabalho para outras
  classes. Geralmente, as fachadas gerenciam o ciclo de vida completo dos
  objetos que usam.
"""


from __future__ import annotations


class Facade:
    """
    Proporciona uma interface simples, abstraindo toda complexidade de
    integração com um ou vários subsistemas.
    """

    def __init__(self) -> None:
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def full_cicle_adjustment(self) -> str:
        """
        Fazendo uso de funções é possivel desenvolver uma lógica arrojada,
        controlando as chamadas para os subsistemas e retornando a resposta
        para o Client.
        """

        results = []

        results.append("Facade: ajuste completo...")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem1.operation_n())

        results.append(self._subsystem2.operation1())
        results.append(self._subsystem2.operation_z())

        return "\n".join(results)

    def video_adjustment(self) -> str:
        results = []
        results.append("Facade: ajustando apenas o vídeo...")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem1.operation_n())

        return "\n".join(results)

    def audio_adjustment(self) -> str:
        results = []
        results.append("Facade: ajustando apenas o audio...")
        results.append(self._subsystem2.operation1())
        results.append(self._subsystem2.operation_z())

        return "\n".join(results)


class Subsystem1:
    """
    Subsistema de tratamento de Vídeo.
    """

    def operation1(self) -> str:
        return "Subsystem1: Tamanho ajustado!"

    def operation_n(self) -> str:
        return "Subsystem1: Filtros aplicados!"


class Subsystem2:
    """
    Subsistema de tratamento de Áudio.
    """

    def operation1(self) -> str:
        return "Subsystem2: Volume nivelado!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Ruído removido!"


def client_code(facade: Facade) -> None:
    """
    O Client interage com os subsistemas através da interface do Facade,
    tornando responsabilidade do mesmo, todo o fluxo de acionamento e
    controle das integrações, reduzindo assim a complexidade do código.
    """

    print(facade.full_cicle_adjustment(), end="\n\n")
    print(facade.video_adjustment(), end="\n\n")
    print(facade.audio_adjustment(), end="")


if __name__ == "__main__":
    facade = Facade()
    client_code(facade)
