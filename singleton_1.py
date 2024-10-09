""""
Caracteristicas do Singleton:
Instancia Unica: Garante que uma classe tenha apenas uma unica instancia durante a execucao do programa.
Acesso Global: Fornece um ponto de acesso global a instancia unica, permitindo que diferentes partes de um aplicativo usem essa instancia sem precisar criar novas.
Controle de Instancia: Controla a criacao e gerenciamento da instancia, normalmente por meio de um metodo estatico que cria a instancia se ela ainda nao existir e a retorna em todas as chamadas subsequentes.
Implementacao Basica:
Para implementar um Singleton em uma linguagem como Java, Python ou C#, normalmente se segue este padrao:

Construtor Privado: Impede que outras classes criem instancias diretamente.
Metodo Estatico: Um metodo estatico que retorna a instancia unica da classe.
Atributo Estatico: Um atributo estatico que armazena a instancia unica.
https://www.informit.com/articles/article.aspx?p=1404056
"""

class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
       self.tema ="O tema escuro"
       self.font = "18px"


if __name__ =="__main__":
    as1  = AppSettings()


    as2 = AppSettings()
    as3 = AppSettings()
    as1.tema ="O tema claro"
    print(as1.tema)

    as1.nome = 'Luiz'
    print(as3.nome)        