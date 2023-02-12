"""
  O Proxy é um padrão de projeto estrutural que fornece um objeto que atua
  como um substituto para um objeto de serviço real usado por um cliente.
  Um proxy recebe solicitações do cliente, realiza alguma tarefa (controle
  de acesso, armazenamento em cache, registro de solicitações, inicialização
  preguiçosa e etc.) e passa a solicitação para um objeto de serviço.
"""

from abc import ABC, abstractmethod
from typing import List, Dict
from time import sleep


class ISubject(ABC):
    """
    Proporciona uma interface comum para o RealSubject e o Proxy, o que
    possibilita o uso do proxy no lugar do objeto real.
    """

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_user_data(self, id: int) -> Dict:
        pass


class RealSubject(ISubject):
    """
    O RealSubject contem a lógica de negócio, geralmente seus processos
    tendem a ser mais pesados e/ou sensíveis.

    Ex: correção ou validação do input. O Proxy pode tratar isso sem que
    o código do RealSubject seja afetado.
    """

    _data = [
        {'name': 'user 1', 'age': 20},
        {'name': 'user 2', 'age': 21},
        {'name': 'user 3', 'age': 22},
    ]

    def __init__(self) -> None:
        self._log = []

    def get_all(self) -> List[Dict]:
      # O sleep está sendo utilizado para simular um processo pesado
        sleep(2)
        return self._data

    def get_user_data(self, id: int) -> Dict:
      # O sleep está sendo utilizado para simular um processo pesado
        sleep(2)
        return self._data[id]


class Proxy(ISubject):
    """
    O Proxy utiliza a mesma interface para que possa interceptar as
    requisições para o RealSubject.

    Existem diversos casos de uso para os proxys, dentre eles:
      - proxy virtual
      - proxy de proteção
      - proxy remoto
      - proxy registro
      - proxy caches
    """

    _subject: RealSubject = None
    _all_users: List[Dict]
    _user = {}

    def instance(self):
        if self._subject is None:
            self._subject = RealSubject()

        return self._subject

    def get_all(self):
        if not hasattr(self, '_all_users'):
            self._all_users = self._subject.get_all()

        return self._all_users

    def get_user_data(self, id: int):
        if self._user != self._all_users[id]:
            self._user = self._subject.get_user_data(id)

        return self._user


def client_code(subject: Proxy) -> None:
    """
    O Client simula uma requisição para os objetos do RealSubject, mas não
    faz uso desta classe diretamente, chamando os métodos apenas pelo Proxy.
    """

    subject.instance()

    # Obtem a informação da RealSubject
    print(f'RealSubject: {subject.get_all()}')
    print(f'RealSubject:  {subject.get_user_data(1)}')

    # Obtendo a mesma informação pelo armazenamento em cache do Proxy
    for i in range(3):
        print(f'Proxy: {subject.get_all()}')
        print(f'Proxy: {subject.get_user_data(1)}')

    # Obtem a informação da RealSubject novamente
    print(f'RealSubject: {subject.get_user_data(2)}')


if __name__ == "__main__":
    print("Client: iniciando chamada dos objetos...")
    proxy = Proxy()
    client_code(proxy)
