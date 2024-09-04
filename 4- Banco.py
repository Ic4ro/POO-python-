import os 

os.system("cls || clear") 

class Conta_Bancaria: 

    def __init__(self, banco: str, agencia: str, numeroDaConta: str, tipoDaConta: str, saldoAtual: float, limiteDisponivel: float) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numeroDaConta = numeroDaConta
        self.tipoDaConta = tipoDaConta
        self.saldoAtual = saldoAtual
        self.limiteDisponivel = limiteDisponivel

      
    def __str__(self) -> str:
        return (f"\nBanco: {self.banco}"
                f"\nAgência: {self.agencia}"
                f"\nNúmero da Conta: {self.numeroDaConta}"
                f"\nTipo da Conta: {self.tipoDaConta}"
                f"\nSaldo Atual: {self.saldoAtual}"
                f"\nLimite Disponível: {self.limiteDisponivel}"                 
                )  

class Funcionario:
    def __init__(self, codigoDoFuncionario: str, nome: str, endereco: str, telefone: str, email: str, contaBanco: Conta_Bancaria) -> None:
        self.codigoDoFuncionario = codigoDoFuncionario
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.contaBanco = contaBanco

    def __str__(self) -> str:
        return  (f"Código do Funcionário: {self.codigoDoFuncionario}"
                f"\nNome: {self.nome}"
                f"\nEndereço: {self.endereco}"
                f"\nTelefone: {self.telefone}"
                f"\nE-mail: {self.email}"
                f"\n=== Conta Bancária ==={self.contaBanco}"
                )


funcionario = Funcionario("123", "Icaro", "Rua A", "071987744788", "icaro123@gmail.com",
                          Conta_Bancaria("Inter", "123", "233", "Corrente", 1500, 4000)) 

print(funcionario)