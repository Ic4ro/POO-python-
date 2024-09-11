from abc import ABC, abstractmethod
import os 

os.system("cls || clear")

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario
    
    @abstractmethod # Decorador
    def salario_final(self) -> float: 
        pass

    def __str__(self) -> str:
        return (f"Nome: {self.nome}"
                f"\nSalário: {self.salario}"
                f"\nSalário Final: {self.salario_final()}"
                )    
    
class Motoboy(Funcionario):
    # Acréscimo de 10%.
    BONIFICACAO = 1.1

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado


class Engenheiro(Funcionario):
    # Acréscimo de 20%.
    BONIFICACAO = 1.2

    def __init__(self, nome: str, salario: float, crea: str) -> None:
        super().__init__(nome, salario)
        self.crea = crea

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado 
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}"
                )


# Instaciando classes.
motoboy_1 = Motoboy("José", 1000)
print(motoboy_1)
print("\n")
engenheiro_1 = Engenheiro("Marta", 1000, "123")
print(engenheiro_1)
