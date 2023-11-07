def verificar_status(media):
    if media > 6:
        return "Aprovado"
    elif 4 <= media <= 6:
        return "Verificação Suplementar"
    else:
        return "Reprovado"

media_aluno = float(input("Digite a média do aluno: "))
status = verificar_status(media_aluno)
print(f"Status do aluno: {status}")
