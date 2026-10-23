import os

caminho_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'estoque.txt')
while True:
    print('\n' + '=' * 40)
    print('     Bem-vindo ao sistema de estoque!')
    print('          MARQUES CONSTRUÇÕES')
    print('      Sistema de controle de materiais')
    print('=' * 40)
    print('1 - Cadastrar material')
    print('2 - Consultar estoque')
    print('3 - Ordenar estoque por nome')
    print('4 - Buscar material')
    print('5 - Sair')
    print('=' * 40)
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        material = input('Qual material deseja casdratrar?')
        material_existe = False
        with open(caminho_estoque, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome_salvo = linha.strip().split(';')[0]
                if nome_salvo.lower() == material.lower():
                    material_existe = True
        if material_existe:
            print('Esse material já está cadastrado!')
        else:
            quantidade = int(input('Digite a quantidade: '))
            with open(caminho_estoque, 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{material};{quantidade}\n')
            print('Material salvo no estoque!')
    elif opcao == '2':
        with open(caminho_estoque, 'r', encoding='utf-8') as arquivo:
            print('\n--- MATERIAIS CADASTRADOS ---')
            print(arquivo.read())

    elif opcao == '4':
        material_procurado = input('Qual material deseja buscar? ')
        encontrado = False
        with open(caminho_estoque, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(';')
                nome_salvo = partes[0]

                if nome_salvo.lower() == material_procurado.lower():
                    encontrado = True
                    quantidade = partes[1]
                    print('Material encontrado:', nome_salvo)
                    print('Quantidade:', quantidade)

        if not encontrado:
            print('Material nao encontrado no estoque')
    elif opcao == '5':
                   print('Encerrando o sistema. até logo!')
                   break 
    elif opcao == '3':
        materiais = []

        with open(caminho_estoque, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                materiais.append(linha.strip())

        for i in range(len(materiais)):
            for j in range(i + 1, len(materiais)):
                nome1 = materiais[i].split(';')[0].lower()
                nome2 = materiais[j].split(';')[0].lower()

                if nome1 > nome2:
                    temporario = materiais[i]
                    materiais[i] = materiais[j]
                    materiais[j] = temporario

        print('Estoque ordenado:')
        for material in materiais:
            print(material)
    input('\nPressione Enter para voltar ao menu...')