import os 

os.system("cls || clear") # limpa o terminal.

# Criando a classe aluno.
class Aluno:
# Criando um construtor.
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade    

    def exibir_dados(self) -> str: 
        return (f"Nome: {self.nome} \n"
                f"Idade: {self.idade}"
                )

# Instanciar class.
aluno = Aluno("Marta", 18)

# print(aluno.nome)
# print(aluno.idade)

print(aluno.exibir_dados())
