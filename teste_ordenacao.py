materiais = [
    'Tijolo;500',
    'Cimento;20',
    'Areia;10',
    'Brita;30'
]

print(materiais)


print(materiais)
for passagem in range(len(materiais) - 1):
    for i in range(len(materiais) - 1):
        nome1 = materiais[i].split(';')[0]
        nome2 = materiais[i + 1].split(';')[0]

        if nome1.lower() > nome2.lower():
            temporario = materiais[i]
            materiais[i] = materiais[i + 1]
            materiais[i + 1] = temporario

print('Estoque ordenado:', materiais)