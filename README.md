# Esteganografia em Imagens com Python

Este projeto explora técnicas de **esteganografia** — a arte de esconder informações dentro de arquivos aparentemente inofensivos, como imagens.

Utilizando Python, foram desenvolvidas duas abordagens para esconder mensagens em imagens e comparar seu impacto em tamanho de arquivo e estrutura binária.

## O que é Esteganografia?

**Esteganografia** é o processo de esconder dados (mensagens, códigos, arquivos) dentro de outros arquivos de forma que a existência da informação oculta passe despercebida.

Diferente da criptografia (que oculta o conteúdo), a esteganografia oculta a **existência** da informação.

Neste projeto, usei imagens como recipiente.

## Sobre os formatos de imagem

Os **formatos de imagem afetam diretamente a capacidade de ocultar dados** e o quanto o arquivo final será alterado.

- 🔸 Recomendado: **PNG**
  - Aceita transparência
  - Sem compressão com perda
  - Preserva melhor os dados ocultos

- 🔸 Evite: **JPEG**
  - Aplica compressão com perda
  - Pode corromper ou destruir dados ocultos

## Métodos Utilizados

### 🔹 **Versão 1 – Anexando código diretamente ao final da imagem**

Neste método, o conteúdo de um arquivo `script.py` é **anexado ao final** da imagem original:

```python
def embutir_codigo(imagem_original, codigo_txt, imagem_saida):
    with open(imagem_original, 'rb') as img, open(codigo_txt, 'rb') as cod:
        conteudo_imagem = img.read()
        conteudo_codigo = cod.read()

    marcador = b'###CODIGO###'
    combinado = conteudo_imagem + marcador + conteudo_codigo

    with open(imagem_saida, 'wb') as out:
        out.write(combinado)

embutir_codigo('imagem_original.jpg', 'script.py', 'imagem_com_codigo.jpg')
```

#### ✅ Vantagens:

- A imagem original **não é alterada** internamente.
- Visualizadores de imagem **ignoram o conteúdo extra** no final do JPEG.
- Tamanho final do arquivo aumenta **apenas pelo conteúdo inserido**.

#### 📊 Exemplo:

- Imagem original: `42.20 KB`
- Imagem com código: `42.23 KB` ➜ aumento de apenas `0.03 KB`

### 🔹 **Versão 2 – Esteganografia com LSB (Least Significant Bit)**

Neste método, utilizamos a biblioteca `stegano` para esconder a mensagem **nos bits menos significativos dos pixels** da imagem.

```python
from stegano import lsb

imagem_codificada = lsb.hide("./imagem_original.jpg","Olá mundo!")
imagem_codificada.save("./imagem_com_stegano.png")
mensagem = lsb.reveal("./imagem_com_stegano.png")
print(f"Mensagem escondida: {mensagem}")
```

#### ⚠️ Características:

- O Stegano **converte a imagem para PNG**, mesmo que o original fosse JPEG.
- A modificação nos pixels é **sutil, mas massiva**.
- O arquivo final é **muito maior**, mesmo para mensagens pequenas.

#### 📊 Exemplo:

- Imagem original: `42.20 KB`
- Imagem com mensagem LSB: `217.42 KB` ➜ aumento de `175.22 KB`

## 🔍 Comparação entre os métodos

| Método                   | Formato Final | Alteração Visual | Tamanho Final   |
|--------------------------|---------------|------------------|------------------|
| Anexar ao final          | `.jpg`        | Nenhuma          | +0.03 KB         |
| LSB com `stegano`        | `.png`        | Nenhuma visível  | +175.22 KB       |
