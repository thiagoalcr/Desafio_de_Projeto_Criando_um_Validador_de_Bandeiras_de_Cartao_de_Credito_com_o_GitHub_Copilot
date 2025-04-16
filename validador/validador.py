def identificar_bandeira(numero_cartao):
    
    if numero_cartao.startswith('4'):
        return "Visa"
    elif numero_cartao[:2] in ['51', '52', '53', '54', '55'] or 2221 <= int(numero_cartao[:4]) <= 2720:
        return "MasterCard"
    elif numero_cartao[:4] in ['4011', '4312', '4389']:  # Adicione outros intervalos de Elo conforme necessário
        return "Elo"
    elif numero_cartao[:2] in ['34', '37']:
        return "American Express"
    elif numero_cartao.startswith('6011') or numero_cartao.startswith('65') or 644 <= int(numero_cartao[:3]) <= 649:
        return "Discover"
    elif numero_cartao.startswith('6062'):
        return "Hipercard"
    elif numero_cartao.startswith('35'):
        return "JCB"
    elif numero_cartao.startswith('50'):
        return "Aura"
    else:
        return "Desconhecida"

if __name__ == "__main__":
    numero = input("Digite o número do cartão de crédito: ")
    bandeira = identificar_bandeira(numero)
    print(f"A bandeira do cartão é: {bandeira}")