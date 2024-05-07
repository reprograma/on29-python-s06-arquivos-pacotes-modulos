with open('meu-arquivo.txt', 'r') as arquivos: #o 'r' significa que realizaremos somente a leitura do arquivo
    conteudo = arquivos.read() #leitura de um arquivo
    print(conteudo)

with open('meu-arquivo.txt', 'w') as arquivo: #o 'w' significa que zeraremos e reescreveremos o arquivo
    arquivo.write("o mundo e legal") #escrita de um arquivo