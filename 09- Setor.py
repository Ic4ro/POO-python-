from enum import Enum
import os 

os.system("cls || clear") 
class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Sexo(Enum):
    MASCULINO = "Masculino | M"
    FEMININO = "Feminino | F"

class Funcionario:
    def __init__(self, id: str, nome: str, salario: float, setor: Setor, sexo: Sexo, idade: int) -> None:
        self.id = id
        self.nome = nome
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
        self.salario = salario
        self.idade = idade
    

    def __str__(self) -> str:
        return (f"Id: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}"
                f"\nSetor: {self.setor.value}"
                f"\nSalário: {self.salario}"
                )
    
funcionario_1 = Funcionario("1233", "Icaro", 1500, Setor.MARKETING, Sexo.MASCULINO, 19)

print(funcionario_1)