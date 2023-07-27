menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair  

 Escolha uma opcao =>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor do seu déposito:"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Déposito: R$ {deposito: .2f}\n"
        else:
            print("Não foi possivel efetuar o déposito")
    elif opcao == "2":
        saque = float(input("Digite o valor do saque: "))
        limite_insuficiente = saque > limite
        limite_maximo_de_saque = numero_saques >= LIMITE_SAQUE
        sem_saldo = saque > saldo

        if limite_insuficiente:
            print("Seu limite é insuficiente, diminua o valor do saque.")
        elif limite_maximo_de_saque:
            print("Você já atingiu o limite de saques. Tente novamente amanhã.")
        elif sem_saldo:
            print("Saldo insuficiente para saque.")
        elif saque > 10:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        else:
            print("Operação falhou. O valor informado é inválido.")
    elif opcao == "3":
           print('\n============EXTRATO===========')
           print('Não foram realizadas movimentações.' if not extrato else extrato)
           print(f"\nSaldo: R$ {saldo:.2f}")
           print("=========================")
    elif opcao == "0":
            print("Saindo...")
            break
    else:
         print("Tente novamente, selecione uma opção válida")

