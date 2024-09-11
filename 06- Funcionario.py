from abc import ABC, abstractmethod
import os 

os.system("cls || clear")

# Criando a classe endereço
class Endereco: 
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nCep: {self.cep}"
                f"\nCidade: {self.cidade}"
                )  

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario = salario
    
    @abstractmethod
    def salario_final(self) -> float: 
        pass

    def __str__(self) -> str:
        return (f"Nome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nSalário: {self.salario}"
                f"\nSalário Final: {self.salario_final()}"
                f"{self.endereco}"      
                )    

class Medico(Funcionario):
    BONIFICACAO = 1.1

    def __init__(self, nome: str, salario: float, crm: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        return self.salario * self.BONIFICACAO

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCRM: {self.crm}"
                )

class Engenheiro(Funcionario):
    BONIFICACAO = 1.2

    def __init__(self, nome: str, salario: float, crea: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        return self.salario * self.BONIFICACAO

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}"
                )


# Instanciando classes
medico_1 = Medico("Icaro", 1000, "123", "071877", "Icaro@gmail.com", 
                  Endereco("Rua A", "23", "2 Andar", "123", "Salvador"))
print(medico_1)

print("\n")

engenheiro_1 = Engenheiro("Icaro", 1000, "123", "0719888", "Icaro@", 
                           Endereco("Rua A", "12", "1 Andar", "123", "Salvador"))
print(engenheiro_1)
