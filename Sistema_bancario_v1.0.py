# Sistema Bancário - Versão 1.0
# Desenvolvedor: Eduardo Kazan

# Configurações iniciais - definição de variáveis de controle do sistema
# Menu de opções - apresentação das opções disponíveis para o usuário
# Contrução de funções - definição das funções para realizar operações bancárias
# realizar_saque    realizar_deposito   exibir_extrato
# Loop do sistema - execução do sistema até que o usuário decida sair
# Exibição de mensagens - feedback ao usuário sobre as operações realizadas
# Finalização - encerramento do sistema com mensagem de despedida

# Configurações iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

# Menu de opções
menu = """
     1. Depositar
     2. Sacar
     3. Extrato
     4. Sair
"""
# Funções do sistema bancário


def realizar_saque(saldo, limite, numero_saques, limite_saques, extrato):
    valor_saque = float(input("Digite o valor do saque: R$ "))
    if valor_saque > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor_saque > limite:
        print("O valor do saque excede o limite permitido.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques diários atingido. Tente novamente amanhã.")
    else:
        saldo -= valor_saque
        numero_saques += 1
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
    return saldo, numero_saques, extrato


def realizar_deposito(saldo, extrato):
    valor_deposito = float(input("Digite o valor do depósito: R$ "))
    if valor_deposito <= 0:
        print("Valor inválido. Por favor, digite um valor maior que zero.")
    else:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
    return saldo, extrato


def exibir_extrato(extrato):
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:".center(60, " "))
        print(extrato)


# Loop principal do sistema
while True:
    print()
    print("BEM-VINDOS AO SISTEMA BANCÁRIO".center(60, " "))
    print("Selecione uma opção:".center(60, " "))

    opcao = input(menu)

    # DEPOSITO
    if opcao == "1":
        print("Opção escolhida: DEPÓSITO".center(60, " "))
        saldo, extrato = realizar_deposito(saldo, extrato)

    # SAQUE
    elif opcao == "2":
        print("Opção escolhida: SAQUE".center(60, " "))
        saldo, numero_saques, extrato = realizar_saque(
            saldo, limite, numero_saques, limite_saques, extrato)

    # EXTRATO
    elif opcao == "3":
        print("Opção escolhida: EXTRATO".center(60, " "))
        exibir_extrato(extrato)

    # SAIR
    elif opcao == "4":
        print("Saindo do sistema... Obrigado por utilizar nossos serviços!")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Tente novamente.")
