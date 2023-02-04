from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
    # Armazena a posição ocupada dentro do objeto
    _position: int = None

    # Indica a direção que o iterador vai seguir
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        Vai até a próxima posição conforme ordenação:
            self._reverse = True ->  retorna 1 posição.
            self._reverse = False ->  avança 1 posição.

        Retornos:
            value -> WordsCollection[self._position]
            S/ Index -> Raise StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    Coleção de dados que implementa fornece formas personalizadas
    para armazenmanto, ordenação e retorno de dados.
    """

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        Sobrescreve o método Iterator padrão, para usar o AlphabeticalOrderIterator.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("Primeiro")
    collection.add_item("Segundo")
    collection.add_item("Terceiro")

    print("Ordem crescente:")
    print("\n".join(collection))
    print("")

    print("Ordem decrescente:")
    print("\n".join(collection.get_reverse_iterator()), end="")
