def embutir_codigo(imagem_original, codigo_txt, imagem_saida):
    with open(imagem_original, 'rb') as img, open(codigo_txt, 'rb') as cod:
        conteudo_imagem = img.read()
        conteudo_codigo = cod.read()

    marcador = b'###CODIGO###'
    combinado = conteudo_imagem + marcador + conteudo_codigo

    with open(imagem_saida, 'wb') as out:
        out.write(combinado)

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

embutir_codigo('../imagem_original.jpg', 'codigo.py', 'imagem_com_codigo.jpg')
extrair_e_executar("imagem_com_codigo.jpg")
