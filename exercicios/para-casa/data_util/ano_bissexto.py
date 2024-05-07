def eh_ano_bissexto(ano):
    if ano%4 == 0:
        if ano%100 != 0:
            return True
        else:
            if ano%400 == 0:
                return True
            else:
                return False
    else:
        return False