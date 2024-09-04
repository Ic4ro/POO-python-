import os 

os.system("cls || clear") # limpa o terminal.

# Criando a classe endereço
class Endereco: 
# Criando um construtor.
    def __init__(self, logradouro: str, numero: str) -> None:
        self.logradouro = logradouro
        self.numero = numero

# Semelhante ao toString().         
    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                )  

# Criando a classe aluno.
class Aluno:

# Criando um construtor.
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco    

    def __str__(self) -> str:
        return (f"Nome: {self.nome} \n"
                f"Idade: {self.idade} \n"
                f"=== Endereço ==={self.endereco}"
                )

# Instanciar class.
# endereco1 = Endereco("Rua A", "255")
# aluno = Aluno("Marta", 18, endereco1)

aluno = Aluno("Icaro", 19, 
              Endereco("Rua A", "25"))

print(aluno)