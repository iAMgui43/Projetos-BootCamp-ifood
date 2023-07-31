import textwrap

def menu():
    menu = """\n

    -----------> MENU <----------
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair

    ==>"""

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Déposito:\tR$ {valor: .2f}\n"
        print("\n=== Déposito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! o valor informado e inválido. @@@")
        
    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques

    if excedeu_saldo: 
        print("\n@@@ Você não tem saldo o suficiente para concluir esse operação. @@@")
    elif excedeu_limite:
        print("\n@@@ Seu limite e insuficiente para esse tipo de operação. @@@")
    elif excedeu_saque:
        print("\n@@@ Você ja realizou o máximo de saques hoje, tente novamente amanhã! @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("=== Saque realizado com sucesso! ====")

    else:
        print("\n @@@ Operação falhou! o valor informado e inválido! @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n----------------------EXTRATO------------------------")
    print("Não foi realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("-------------------------------------------------------")

def criar_usuarios(usuarios):
    cpf = input("Informe seu CPF (somente números):") 
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um usuario com esse cpf @@@")
        return

    nome = input("Informe seu nome completo:")
    data_nascimento = input("informe sua data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouron nro - bairro - cidade/sigla do estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuario criado com sucesso ===")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o cpf do usuario:")
    usuario = filtrar_usuarios(cpf, usuarios) 

    if usuario:
        print("\n=== Conta Criada com Sucesso ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado fluxo de criação de contas encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C\C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor de déposioto:"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor de saque:"))

            saldo, extrato = sacar (
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            criar_usuarios(usuarios)

        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
             contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            print("Saindo ...")
            break
        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

main()