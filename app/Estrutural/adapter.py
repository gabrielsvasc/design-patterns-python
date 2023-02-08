"""
    O Adapter atua como um wrapper entre dois objetos. Ele captura chamadas
    para um objeto e as deixa reconhecíveis tanto em formato como interface
    para este segundo objeto.

    Identificação: O adapter é reconhecível por um construtor que utiliza
    uma instância de tipo abstrato/interface diferente. Quando o adaptador
    recebe uma chamada para qualquer um de seus métodos, ele converte
    parâmetros para o formato apropriado e direciona a chamada para um ou
    vários métodos do objeto envolvido.
"""


class Target:
    """
    O Target representa a classe base com uma interface bem definida.
    """

    def request(self) -> str:
        return "Target: execução padrão do método."


class Adaptee:
    """
    O Adaptee possui um método útil para o Cliet, porém possui uma
    interface incompatível, sendo assim seus métodos precisam ser
    acessados através de um Adapter.
    """

    def specific_request(self) -> str:
        return "execução padrão do método na classe incompatível."


class Adapter(Target, Adaptee):
    """
    O Adapter torna a interface Adaptee compatível com a Target, utilizando
    herança múltipla.
    """

    def request(self) -> str:
        return f"Adapter: [Adaptee] {self.specific_request()}"


def client_code(target: Target) -> None:
    """
    Respresentação do Client Code.
    """

    print(target.request())


if __name__ == "__main__":
    target = Target()
    client_code(target)

    adapter = Adapter()
    client_code(adapter)
