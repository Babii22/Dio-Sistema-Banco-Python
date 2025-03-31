import textwrap


def menu():
    menu = """
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n-- A operação falhou! O valor informado é inválido. --")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("\n-- Limite de saques diários atingido. --")
    elif valor > saldo:
        print("\n-- Saldo insuficiente. --")
    elif valor > limite:
        print(f"\n-- O limite por saque é de R$ {limite:.2f}. --")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n-- A operação falhou! O valor informado é inválido. --")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")


def main():
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500

    saldo = 0.0
    extrato = []
    numero_saques = 0

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_SAQUE_VALOR,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "0":
            print("Obrigado por utilizar nosso banco!")
            break

        else:
            print("Operação inválida. Tente novamente.")


if __name__ == "__main__":
    main()
