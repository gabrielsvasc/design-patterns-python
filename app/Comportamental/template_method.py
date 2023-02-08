"""
    O Template Method é um padrão de projeto comportamental
    que permite definir o esqueleto de um algoritmo em uma
    classe base e permitir que as subclasses substituam as
    etapas sem alterar a estrutura geral do algoritmo.

    Identificação: O Template Method pode ser reconhecido por
    métodos comportamentais que já possuem um comportamento
    “padrão” definido pela classe base.
"""


from abc import ABC, abstractmethod


class IDataMiner(ABC):
    """
    Classe abstrata que define um template_method responsável pela estrutura
    dos algoritmos, realiza a chamada dos métodos, sendo eles os com implementação
    padrão (analyze_data & send_report), os abstrados que são definidos pelas
    subclasses (open_file & extract_data) e pontos de extensão para a classe.
    """

    def template_method(self) -> None:
        """
        Define toda estrutura de execução.
        """

        self.open_file()
        self.analyze_data()
        self.hook1()
        self.extract_data()
        self.send_report()
        self.hook2()

    # Métodos com implementação padrão para todas subclasses.

    def analyze_data(self) -> None:
        print("IDataMiner: Análisando os dados do arquivo...")

    def send_report(self) -> None:
        print("IDataMiner: Enviando relatório com a quantidade de linhas extraídas...")

    # Métodos que devem ser definidos pelas subclasses.

    @abstractmethod
    def open_file(self) -> None:
        pass

    @abstractmethod
    def extract_data(self) -> None:
        pass

    # Métodos que permitem a extensão das funcionalidades da interface.

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class PDFDataMIner(IDataMiner):
    """
    Classe que implementa os métodos abstratos da interface.
    """

    def open_file(self) -> None:
        print("PDFDataMIner: Abrindo PDF...")

    def extract_data(self) -> None:
        print("PDFDataMIner: Extraindo palavras chave do PDF...")


class CSVDataMiner(IDataMiner):
    """
    Classe que implementa os métodos abstratos e extente as funcionalidades utilizando Hooks.
    """

    def open_file(self) -> None:
        print("CSVDataMiner: Abrindo CSV...")

    def extract_data(self) -> None:
        print("CSVDataMiner: Extraindo as linhas das colunas de NF, Valor e Vencimento...")

    def hook1(self) -> None:
        print("CSVDataMiner (HOOK): Ordenando por NF...")

    def hook2(self) -> None:
        print(
            "CSVDataMiner (HOOK): Separando por data de vencimento...")


def client_code(abstract_class: IDataMiner) -> None:
    """
    Responsável por receber o classe concreta e executar o template_method.
    """
    abstract_class.template_method()


if __name__ == "__main__":
    # Extrai os dados de um arquivo PDF
    client_code(PDFDataMIner())
    print("\n")

    # Extrai os dados de um arquivo CSV
    client_code(CSVDataMiner())
