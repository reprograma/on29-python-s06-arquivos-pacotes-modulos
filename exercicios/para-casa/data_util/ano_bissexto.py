def calcular_ano_bissexto():
  # vamos solicitar que o usuário informe um ano
  ano = int(input("Informe o ano: "))
     
  # vamos verificar se o ano informado é bissexto
  if(((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0)):
    print("\nO ano informado é bissexto.\n")
  else:
    print("\nO ano informado não é bissexto.\n");
 
