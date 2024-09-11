import os 

os.system("cls || clear")

class Pets: 
    def __init__(self, nome: str, idade: int, raca: str, porte: str, alimentacao: str) -> None:
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

    def exibir_dados(self) -> str: 
        return (f"Nome: {self.nome} \n"
                f"Idade: {self.idade} \n"
                f"Raça: {self.raca} \n"
                f"Porte: {self.porte} \n"
                f"Alimentação: {self.alimentacao} \n"
                )
    
pets1 = Pets("Totó", 8, "Pit Bull", "Grande", "Rafael")    
pets2 = Pets("Thor", 6, "Poodle", "Médio","TUDO QUE VÊ PELA FRENTE")

print(pets1.exibir_dados())
print(pets2.exibir_dados())
