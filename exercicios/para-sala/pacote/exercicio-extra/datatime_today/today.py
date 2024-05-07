from datetime import datetime

def today(opcao = "sem-hora"):
    return datetime.today().strftime('%d-%m-%Y %H:%M:%S') if opcao == "hora" else datetime.today().strftime('%d-%m-%Y')
    
    
    
