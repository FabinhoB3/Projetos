menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
Selecione uma opção => 
"""
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
        valor = float(input("Informe o valor do Deposito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Novo Saldo: R$ {saldo:.2f}")
        else:
            print("Operação falhou! O valor informado invalido.")
        #_______
    elif opcao == 2:
        print("Saque")
        #_______
        valor = float(input("Informe o valor de Saque: R$ "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Operação falhou! Você não tem saldo suficiente. \n Saldo: R$ {saldo}")
        
        elif excedeu_limite:
            print(f"Operação falhou! O valor de saque excede o limite. \n Limite de saque: {limite}")

        elif excedeu_saque:
            print("Operação falhou! Número maximo de saques diarios excedidos! Volte amanhã.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nNovo saldo: R$ {saldo:.2f}")
            print(f"Numero de Saques diarios efetuados {numero_saques}  | MAXIMO: {LIMITE_SAQUES} ")
        
        else:
            print("Operação falhou: O valor informado é invalido")
        #_______
    elif opcao == 3:
        #_______
        print("\n============= EXTRATO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        #_______
    elif opcao == 0:
        break
    else:
        print("Opeção invalida, por favor selecione novamente a operação desejada.")


