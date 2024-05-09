# **Exercício 1: Leitura de um arquivo TXT**

# with open('MeuArquivo.txt','r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)
    
with open("MeuArquivo.txt", "w") as NovoArquivo:
    conteudo = NovoArquivo.write("Estudando Python!")
    

