# Esteganografia em Imagens com Python

Este projeto explora técnicas de **esteganografia** — a arte de esconder informações dentro de arquivos aparentemente inofensivos, como imagens ou documentos.

Utilizando Python, foram desenvolvidas três abordagens para esconder dados em arquivos e observar o impacto em tamanho, estrutura e comportamento.

## O que é Esteganografia?

**Esteganografia** é o processo de esconder dados (mensagens, códigos, arquivos) dentro de outros arquivos, de forma que a **existência** dessas informações passe despercebida.

Diferente da criptografia (que oculta o conteúdo da informação), a esteganografia oculta o **fato de que a informação existe**.

## Sobre os formatos de imagem

Os **formatos de imagem afetam diretamente a capacidade de ocultar dados** e o quanto o arquivo final será alterado.

- 🔸 **Recomendado: PNG**
  - Sem compressão com perda
  - Preserva dados ocultos com mais fidelidade
  - Aceita transparência

- 🔸 **Evite: JPEG**
  - Aplica compressão com perda
  - Pode corromper ou destruir dados ocultos

## Métodos Utilizados

### 🔹 Versão 1 – Anexando código ao final da imagem

Neste método, um arquivo `codigo.py` é anexado **diretamente ao final** de uma imagem, sem alterar sua estrutura visível.

```python
def embutir_codigo(imagem_original, codigo_txt, imagem_saida):
    with open(imagem_original, 'rb') as img, open(codigo_txt, 'rb') as cod:
        conteudo_imagem = img.read()
        conteudo_codigo = cod.read()

    marcador = b'###CODIGO###'
    combinado = conteudo_imagem + marcador + conteudo_codigo

    with open(imagem_saida, 'wb') as out:
        out.write(combinado)
```

#### Vantagens

- A imagem continua visualizável normalmente.
- Visualizadores de imagem ignoram os dados extras.
- Alteração mínima no tamanho do arquivo.

#### Exemplo

- Imagem original: `42.20 KB`  
- Com código oculto: `42.23 KB` ➜ aumento de apenas `0.03 KB`

### 🔹 Versão 2 – Esteganografia com LSB (Least Significant Bit)

Neste método, utilizamos a biblioteca `stegano` para esconder a mensagem **nos bits menos significativos dos pixels** da imagem.

```python
from stegano import lsb

imagem_codificada = lsb.hide("./imagem_original.jpg", "Olá mundo!")
imagem_codificada.save("./imagem_com_codigo.png")
mensagem = lsb.reveal("./imagem_com_codigo.png")
print(f"Mensagem escondida: {mensagem}")
```

#### Características

- A imagem original é convertida para PNG.
- A alteração visual é imperceptível, mas ocorre em muitos pixels.
- O tamanho do arquivo cresce consideravelmente, mesmo com mensagens curtas.

#### Exemplo

- Imagem original: `42.20 KB`  
- Com LSB: `217.42 KB` ➜ aumento de `175.22 KB`

### 🔹 Versão 3 – Simulação com Arquivo SFX (Self-Extracting Executable)

Nesta abordagem, simulamos uma técnica de engenharia social combinada com esteganografia funcional.

Criamos um arquivo `.exe` autoextraível (SFX) que contém:

- Um **PDF legítimo**, que é aberto normalmente.
- Um **script auxiliar** (simulando código malicioso) que coleta informações do sistema e as envia por e-mail.

Este SFX é disfarçado com **ícone e nome de PDF**, induzindo o usuário a acreditar que está abrindo apenas um documento comum.

```txt
📂 Conteúdo embutido:
  ├── arquivo.pdf         # Documento real
  └── script.exe          # Código oculto que envia informações por e-mail
```

#### Funcionamento

- Ao abrir o `.exe`, o conteúdo é extraído para a pasta de Downloads.
- O **PDF é aberto normalmente**.
- Em segundo plano, o `script.exe` é executado automaticamente.

#### Objetivo

Explorar o conceito de **esteganografia prática e engenharia social**, ocultando o comportamento real de um arquivo por trás de uma aparência inofensiva.

#### Aviso

> ❗ Esta versão é apenas uma **simulação educacional**. Técnicas semelhantes podem ser usadas para propósitos maliciosos, o que é ilegal e antiético. Este projeto é voltado apenas para **estudo e pesquisa de segurança da informação**.

## Conclusão

Este projeto mostra como técnicas de esteganografia podem ser aplicadas de diferentes formas — seja em nível de bits ou na engenharia da entrega de arquivos — para ocultar a existência de informações. É fundamental entender os usos éticos e educativos dessas técnicas, especialmente em um mundo onde a segurança da informação se tornou essencial.
