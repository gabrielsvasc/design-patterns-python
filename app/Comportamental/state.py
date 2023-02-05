"""
  O State é um padrão de projeto comportamental que permite
  que um objeto altere o comportamento quando seu estado
  interno for alterado.

  Identificação: O padrão State pode ser reconhecido por métodos
  que alteram seu comportamento, dependendo do estado dos objetos,
  controlados externamente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class OrderContext:
    """
        Reponsável por manter uma referência para a classe de State,
        além de regular as mudanças de estado.
    """
    _state = None

    def __init__(self, state: IOrderState) -> None:
        self.transition_to(state)

    def transition_to(self, state: IOrderState) -> None:
        """
        Responsável por alterar o State da instância para o OrderState passado no método.
        """

        print(
            f"OrderContext: Alterando {type(self._state).__name__} para {type(state).__name__}...")
        self._state = state
        self._state.context = self

    # Funções responsáveis por acionar os métodos dentro das classes concretas.
    def pending(self):
        self._state.pending()

    def approve(self):
        self._state.approve()

    def reject(self):
        self._state.reject()


class IOrderState(ABC):
    """
    Interface responsável por declarar todos os métodos da classe concreta,
    além de fornecer uma referência ao Context, garantindo que os States
    possam a utilizar para mudar o OrderContext de estado.
    """

    @property
    def context(self) -> OrderContext:
        return self._context

    @context.setter
    def context(self, context: OrderContext) -> None:
        self._context = context

    @abstractmethod
    def pending(self) -> None:
        pass

    @abstractmethod
    def approve(self) -> None:
        pass

    @abstractmethod
    def reject(self) -> None:
        pass


# Classe concreta de estado Aprovado.
class PaymentApproved(IOrderState):
    def pending(self) -> None:
        self.context.transition_to(PaymentPending())
        print("PaymentApproved: Alterado para PENDENTE.")

    def approve(self) -> None:
        print("PaymentApproved: Pagamento já está aprovado!")

    def reject(self) -> None:
        self.context.transition_to(PaymentRejected())
        print("PaymentApproved: Alterado para REJEITADO.")


# Classe concreta de estado Rejeitado.
class PaymentRejected(IOrderState):
    def pending(self) -> None:
        self.context.transition_to(PaymentPending())
        print("PaymentRejected: Alterado para PENDENTE.")

    def approve(self) -> None:
        self.context.transition_to(PaymentApproved())
        print("PaymentRejected: Alterado para APROVADO.")

    def reject(self) -> None:
        print("PaymentRejected: Pagamento já está rejeitado!")


# Classe concreta de estado Pendente.
class PaymentPending(IOrderState):
    def pending(self) -> None:
        print("PaymentPending: Pagamento já está pendente!")

    def approve(self) -> None:
        self.context.transition_to(PaymentApproved())
        print("PaymentPending: Alterado para APROVADO.")

    def reject(self) -> None:
        self.context.transition_to(PaymentRejected())
        print("PaymentPending: Alterado para REJEITADO.")


if __name__ == "__main__":
    context = OrderContext(PaymentPending())
    context.approve()
    context.reject()
    context.reject()
