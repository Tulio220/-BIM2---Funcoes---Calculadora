import math

def calcular_combinacoes(N, M):
    combinacoes = math.factorial(N) / (math.factorial(M) * math.factorial(N - M))
    return combinacoes

N = int(input("Digite o número total de alunos: "))
M = int(input("Digite o número de alunos em um dos grupos: "))

numero_combinacoes = calcular_combinacoes(N, M)
print(f"O número de combinações possíveis é: {numero_combinacoes}")