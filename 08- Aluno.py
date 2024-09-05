from enum import Enum
import os 

os.system("cls || clear") 

class Sexo(Enum):
    MASCULINO = "Masculino | M"
    FEMININO = "Feminino | F"

class Aluno:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade   
        self.sexo = sexo 

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}"
                )
    
aluno_1 = Aluno("Icaro", 19, Sexo.MASCULINO)

print(aluno_1)