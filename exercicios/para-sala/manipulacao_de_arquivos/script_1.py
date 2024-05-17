# Crie um arquivo de texto chamado "dados.txt" 
# com algumas linhas de texto. Escreva um 
# programa em Python que leia o conteúdo
# do arquivo e exiba-o na tela.
 

with open('dados_1.txt','r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open ('dados_1.json', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
