
def eh_ano_bissexto():
  ano = input("Digite o ano: ")
  if (int(ano) % 4) == 0:
    if (int(ano) % 100) == 0:
      if (int(ano) % 400) == 0:
        return True 
      else:
        return False
    else:
      return True
  else:
    return False

print(eh_ano_bissexto())