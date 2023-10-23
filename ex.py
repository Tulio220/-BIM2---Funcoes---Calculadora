# Função para somar dois números
def somar(memoria, numero):
    return memoria + numero

# Função para subtrair dois números
def subtrair(memoria, numero):
    return memoria - numero

# Função para multiplicar dois números
def multiplicar(memoria, numero):
    return memoria * numero

# Função para dividir dois números
def dividir(memoria, numero):
    if numero != 0:
        return memoria / numero
    else:
        print("Erro: divisão por zero!")
        return memoria

# Estado inicial da memória
memoria = 0

# Loop principal do programa
while True:
    print("Estado da memória:", memoria)
    print("Opções:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Limpar memória")
    print("6. Sair do programa")

    # Solicitação da opção do usuário
    opcao = input("Qual opção você deseja? ")

    # Verifica a opção escolhida pelo usuário e executa a operação correspondente
    if opcao == "1":
        numero = float(input("Digite o número a ser somado: "))
        memoria = somar(memoria, numero)
    elif opcao == "2":
        numero = float(input("Digite o número a ser subtraído: "))
        memoria = subtrair(memoria, numero)
    elif opcao == "3":
        numero = float(input("Digite o número a ser multiplicado: "))
        memoria = multiplicar(memoria, numero)
    elif opcao == "4":
        numero = float(input("Digite o número pelo qual dividir: "))
        memoria = dividir(memoria, numero)
    elif opcao == "5":
        memoria = 0
        print("Memória limpa.")
    elif opcao == "6":
        print("Programa encerrado. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")