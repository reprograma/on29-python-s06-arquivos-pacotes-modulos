def inverter_string(s):
    return s[::-1]

def contar_palavras(s):
    return len(s.split())

def verificar_palindromo(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]