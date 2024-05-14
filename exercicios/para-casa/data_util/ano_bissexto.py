'''
Contém uma função eh_ano_bissexto(ano) que verifica se um ano é bissexto e retorna True ou False.
'''
from datetime import date 
def eh_ano_bissexto(ano_bissexto):
    
   if ano_bissexto % 4 == 0 and ano_bissexto % 100 != 0 or ano_bissexto % 400 ==0:
       return True
   else:
       False
        
        
    
        
