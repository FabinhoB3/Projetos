menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
Selecione uma opção => """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))
    
    if opcao == 1:
        print("Depósito")
        #_______
        deposito = float(input("Informe o valor do Deposito: R$ "))
        if deposito <= 0:
            print("Informe um valor valido!")
        else:
            saldo = saldo + deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            print(f"Novo Saldo: R$ {saldo}")

        #_______
    elif opcao == 2:
        print("Saque")
        #_______
        saque = float(input("Informe o valor do Saque: R$ "))
        if saldo >= saque and numero_saques < 3 and saque <= limite and saque > 0:
            saldo = saldo - saque
            print(f"Novo Saldo: {saldo}")
            numero_saques = numero_saques + 1
            print(f"Numero de Saque diarios disponiveis: {LIMITE_SAQUES - numero_saques}")
            extrato += f"Saque: R$ {saque:.2f}\n"
        elif saque > limite:
            print("|| Operação Invalida! Valor de saque maior que 500")
        elif saldo <= saque:
            print(f"|| Operação Invalida! Valor de Saque maior que Saldo. \n Saldo: {saldo} ")
            print(f"Numero de Saque diarios disponiveis: {LIMITE_SAQUES - numero_saques}")
            break
        elif numero_saques >= 3:
            print("|| Operação Invalida! Quantidade de Saques diarios excedidos. Aguarde 24h para efetuar novo saque.")
            print(f"Numero de Saque diarios disponiveis: {LIMITE_SAQUES - numero_saques}")
        else:
            print("Informe um valor valido")
        #_______
    elif opcao == 3:
        print("Extrato")
        #_______
        print("\n============= EXTRATO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        #_______
    elif opcao == 0:
        break
    else:
        print("Opeção invalida, por favor selecione novamente a operação desejada.")


