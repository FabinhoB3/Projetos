def menu():
    menu = """\n
============== MENU ============      
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tCriar Usuario
[5]\tCriar Conta
[6]\tListar Contas

[0]\tSair
Selecione uma opção => """
    return int(input(menu))

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Informe um valor valido!")
        return saldo, extrato
    else:
        saldo = saldo + valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print(f"Novo Saldo: R$ {saldo}")
        return saldo, extrato
        
def sacar(*, saldo, valor, extrato, limite, numero_saques,limite_saques):
    if saldo >= valor and numero_saques < 3 and valor <= limite and valor > 0:
        saldo = saldo - valor
        print(f"Novo Saldo: {saldo}")
        numero_saques = numero_saques + 1
        print(f"Numero de Saque diarios disponiveis: {limite_saques - numero_saques}")
        extrato += f"Saque: R$ {valor:.2f}\n"
        return saldo, extrato, numero_saques
    elif valor > limite:
        print("|| Operação Invalida! Valor de saque maior que 500")
        return saldo, extrato, numero_saques
    elif saldo <= valor:
        print(f"|| Operação Invalida! Valor de Saque maior que Saldo. \n Saldo: {saldo} ")
        print(f"Numero de Saque diarios disponiveis: {limite_saques - numero_saques}")
        return saldo, extrato, numero_saques
    elif numero_saques >= 3:
        print("|| Operação Invalida! Quantidade de Saques diarios excedidos. Aguarde 24h para efetuar novo saque.")
        print(f"Numero de Saque diarios disponiveis: {limite_saques - numero_saques}")
        return saldo, extrato, numero_saques
    else:
        print("Informe um valor valido")
        return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *,extrato):
    print("\n============= EXTRATO ===========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n@@@ Já existe usuario com esse CPF! @@@")
        return # RETORNA PARA A FUNÇÃO PRINCIPAL MAIN()
     
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o edereço (Logradouro, nr - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
   
    print("Usuario criado com sucesso! ")     

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuario: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\n Conta criada com sucesso!")
          return {"agencia": agencia, "numero_conta": numero_conta,"usuario": usuario}
     
     print("\nUsuario não encontrado, fluxo de criação de conta encerrado!")
     
def listar_contas(contas):
     for conta in contas:
          linha = f"""\
                Agencia:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titutal:\t\t{conta['usuario']['nome']}
          """
          print("=" * 100)
          print(linha)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    

    while True:
        opcao = int(menu())
        
        if opcao == 1:#Deposito
            valor = float(input("Informe o valor do Saque: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

                #_______
        elif opcao == 2:#Saque
                valor = float(input("Informe o valor do Saque: R$ "))
                saldo,extrato, numero_saques = sacar(
                     saldo = saldo,
                     valor = valor,
                     extrato = extrato,
                     limite = limite,
                     numero_saques = numero_saques,
                     limite_saques = LIMITE_SAQUES
                )


                #_______
        elif opcao == 3:#Extrato
                exibir_extrato(
                    saldo, extrato = extrato
                )
        elif opcao == 4:
             criar_usuario(usuarios)
        elif  opcao == 5:
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)

             if conta:
                  contas.append(conta)
        elif opcao == 6:
            listar_contas(contas)
            
        elif opcao == 0:#Sair
                break
        else:#Opção invalida
                print("Opeção invalida, por favor selecione novamente a operação desejada.")

main()




