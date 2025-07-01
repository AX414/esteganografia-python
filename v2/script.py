from stegano import lsb

imagem_codificada = lsb.hide("../imagem_original.jpg","Olá mundo!")
imagem_codificada.save("./imagem_com_codigo.png")
mensagem = lsb.reveal("./imagem_com_codigo.png")
print(f"Mensagem escondida: {mensagem}")

