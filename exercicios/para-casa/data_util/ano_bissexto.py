def eh_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    else:
        return False



#De 4 em 4 anos é ano bissexto.
#De 100 em 100 anos não é ano bissexto.
#De 400 em 400 anos é ano bissexto.

#São bissextos todos os anos múltiplos de 400, p.ex.: 1600, 2000, 2400, 2800...

#São bissextos todos os múltiplos de 4, mas que não são multiplos de 100 ao msm tempo (ou seja, o último ano de cada século)
#Se for multiplo de 4, 100 e 400 é bissexto
#Todo ano multiplo de 4 é multiplo de 400
#Não são bissextos anos ímpares e anos pares não múltiplos de 4.
#Prevalecem as últimas regras sobre as primeiras.


#Fonte https://learn.microsoft.com/pt-br/office/troubleshoot/excel/determine-a-leap-year
