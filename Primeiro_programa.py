menu = ""
Saldo = 0
Limite = 1500
Extrato = ""
numero_Saques = 0
numero_saque = 3
limete_saques = 3
deposito = 0
saque = 0
def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """
    return menu
def depositar(saldo , deposito):
    if deposito > 0:
        saldo += deposito
        print(f"Você depositou R${deposito:.2f} reais.")
        print(f"Seu saldo atual é de R${saldo:.2f} reais.")
    else:
        print("Valor inválido para depósito.")
    return saldo
def sacar(saldo, saque, limite, extrato, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if saque > 0 and saque <= limite:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
            print(f"Você sacou R${saque:.2f} reais.")
            print(f"Seu saldo atual é de R${saldo:.2f} reais.")
        else:
            print("Valor inválido para saque.")
    else:
        print("Número máximo de saques atingido.")
    return saldo, extrato, numero_saques
def exibir_extrato(saldo, extrato):
    print("=== Extrato ===")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo: R${saldo:.2f} reais.")
    print("================")
def main():
    global Saldo, Extrato, numero_Saques, deposito, saque
    while True:
        print(menu())
        opcao = input("Escolha uma opção: ").strip().lower()
        if opcao == 'd':
            deposito = float(input("Digite o valor a ser depositado: "))
            Saldo = depositar(Saldo, deposito)
        elif opcao == 's':
            saque = float(input("Digite o valor a ser sacado: "))
            Saldo, Extrato, numero_Saques = sacar(Saldo, saque, Limite, Extrato, numero_Saques, limete_saques)
            Limite_saques = 3 - numero_Saques
            print(f"Você ainda pode sacar {Limite_saques} vezes.")
        elif opcao == 'e':
            exibir_extrato(Saldo, Extrato)
        elif opcao == 'q':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()

    


