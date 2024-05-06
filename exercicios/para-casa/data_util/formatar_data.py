def formatar_data(data):
    partes = data.split('/')
    return f"{partes[2]}-{partes[1]}-{partes[0]}"