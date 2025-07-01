def extrair_e_executar(path_img):
    with open(path_img, 'rb') as f:
        conteudo = f.read()

    marcador = b'###CODIGO###'
    idx = conteudo.find(marcador)
    if idx != -1:
        codigo = conteudo[idx + len(marcador):].decode()
        exec(codigo)
    else:
        print("Nenhum código encontrado.")

extrair_e_executar("imagem_com_codigo.jpg")
