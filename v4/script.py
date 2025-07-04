# Dicionário original
trithemius_dict = {
    'A': "no céu",
    'B': "para todo o sempre",
    'C': "um mundo sem fim",
    'D': "numa infinidade",
    'E': "perpetuamente",
    'F': "por toda a eternidade",
    'G': "durável",
    'H': "incessantemente",
    'I': "irrevogavelmente",
    'J': "irrevogavelmente",
    'K': "eternamente",
    'L': "na sua glória",
    'M': "na sua luz",
    'N': "no paraíso",
    'O': "hoje",
    'P': "na sua divindade",
    'Q': "em Deus",
    'R': "na sua felicidade",
    'S': "no seu reino",
    'T': "na sua majestade",
    'U': "na sua beatitude",
    'V': "na sua beatitude",
    'W': "na sua beatitude",
    'X': "na sua magnífica",
    'Y': "ao trono"
    # Z não tem valor, então só apaguei ele
}

# Inversão do dicionário (para decodificação)
decode_dict = {}
for k, v in trithemius_dict.items():
    if v not in decode_dict:
        decode_dict[v] = k

# Codificador
def ave_maria_trithemius(texto):
    resultado = []
    for char in texto.upper():
        if char in trithemius_dict:
            resultado.append(trithemius_dict[char])
        elif char.isspace():
            resultado.append('\n')  # quebra real de linha
        else:
            resultado.append(char)
    # Une cada item, respeitando quebras de linha reais
    return '\n'.join(' '.join(linha.split()) for linha in ' '.join(resultado).split('\n'))

# Decodificador
def trithemius_decode(texto_codificado):
    palavras = texto_codificado.split()
    buffer = []
    resultado = []

    for palavra in palavras:
        buffer.append(palavra)
        tentativa = ' '.join(buffer)
        if tentativa in decode_dict:
            resultado.append(decode_dict[tentativa])
            buffer = []  # limpa buffer após decodificação
    return ''.join(resultado)

# Menu principal
def main():
    while True:
        print("\n\n<MENU>")
        print("1 - Codificar mensagem")
        print("2 - Decodificar mensagem")
        print("0 - Sair")
        try:
            op = input("\nEscolha uma opção:\nR.: ").strip()
            if op == '1':
                mensagem = input("\nInsira sua mensagem:\nR.: ").strip()
                codificada = ave_maria_trithemius(mensagem)
                print("\n<Mensagem Codificada>\n")
                print(codificada)
            elif op == '2':
                codificada = input("\nInsira a mensagem codificada:\nR.: ").strip()
                decodificada = trithemius_decode(codificada)
                print("\n<Mensagem Decodificada>\n")
                print(decodificada)
            elif op == '0':
                print("\nEncerrando o programa.\n")
                break
            else:
                print("\nOpção inválida.\n")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
