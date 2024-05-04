with open('meu-arquivo.txt', 'r') as arquivos:
    conteudo = arquivos.read()

    print(conteudo)

with open('meu-arquivo.txt', 'w') as arquivo:
    arquivo.write('o mundo é legal')