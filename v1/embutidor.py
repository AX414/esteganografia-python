def embutir_codigo(imagem_original, codigo_txt, imagem_saida):
    with open(imagem_original, 'rb') as img, open(codigo_txt, 'rb') as cod:
        conteudo_imagem = img.read()
        conteudo_codigo = cod.read()

    marcador = b'###CODIGO###'
    combinado = conteudo_imagem + marcador + conteudo_codigo

    with open(imagem_saida, 'wb') as out:
        out.write(combinado)

embutir_codigo('imagem_original.jpg', 'script.py', 'imagem_com_codigo.jpg')