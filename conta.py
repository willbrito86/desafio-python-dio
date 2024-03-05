import msvcrt  # Importando a biblioteca msvcrt para lidar com a entrada de usuário no Windows

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')

    def saque(self, valor):
        if valor > 0:
            if valor <= 500 and len(self.saques) < 3:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.saques.append(valor)
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                print('Limite de saques diários excedido ou valor máximo de saque ultrapassado.')
        else:
            print('Valor inválido para saque.')

    def extrato(self):
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            print('Extrato:')
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo atual: R$ {self.saldo:.2f}')


# Função para obter a entrada do usuário
def obter_input():
    key = msvcrt.getch()  # Capturando a tecla pressionada
    return key.decode('utf-8')  # Convertendo a tecla para string

# Função para exibir o menu e interagir com o usuário
def exibir_menu():
    print('\nMenu:')
    print('1. Depósito')
    print('2. Saque')
    print('3. Extrato')
    print('4. Sair')
    return obter_input()  # Usando a função de entrada personalizada

conta = ContaBancaria()

# Loop principal do programa
while True:
    opcao = exibir_menu()

    if opcao == '1':
        valor = float(input('Digite o valor do depósito: '))
        conta.deposito(valor)
    elif opcao == '2':
        valor = float(input('Digite o valor do saque: '))
        conta.saque(valor)
    elif opcao == '3':
        conta.extrato()
    elif opcao == '4':
        print('Saindo do programa. Obrigado!')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')

