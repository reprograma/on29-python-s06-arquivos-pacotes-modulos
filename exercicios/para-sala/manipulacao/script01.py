with open('meu-arquivo.txt', 'r') as arquivos:
    conteudo = arquivos.read()

    print(conteudo)

with open('meu-arquivo.txt', 'w') as arquivo:
    arquivo.write('ola, mundo!')
# com o 'w' ele apagaa a informação que tem no arquivo e substitui oq estamos colocando
