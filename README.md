# Esteganografia com Python

Este projeto explora técnicas de **esteganografia** — a arte de esconder informações dentro de arquivos aparentemente inofensivos, como imagens ou documentos.

Utilizando Python, foram desenvolvidas **quatro abordagens** para esconder dados em arquivos e observar o impacto em tamanho, estrutura e comportamento.

## O que é Esteganografia?

**Esteganografia** é o processo de esconder dados (mensagens, códigos, arquivos) dentro de outros arquivos, de forma que a **existência** dessas informações passe despercebida.

> Diferente da criptografia (que oculta o conteúdo), a esteganografia oculta o **fato de que a informação existe**.

## Sobre os formatos de imagem

Os **formatos de imagem afetam diretamente a capacidade de ocultar dados**:

- **Recomendado: PNG**
  - Sem compressão com perda
  - Preserva dados ocultos com mais fidelidade
  - Aceita transparência

- **Evite: JPEG**
  - Compressão com perda
  - Pode destruir dados ocultos (especialmente com LSB)

## Métodos Utilizados

### 🔹 Versão 1 – Anexando código ao final da imagem

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
- Alteração mínima no tamanho do arquivo.
- Compatível com PNG e JPEG.

### 🔹 Versão 2 – Esteganografia com LSB (Least Significant Bit)

```python
from stegano import lsb

imagem_codificada = lsb.hide("original.png", "mensagem secreta")
imagem_codificada.save("saida.png")
mensagem = lsb.reveal("saida.png")
print(mensagem)
```

#### Características
- Visualmente imperceptível.
- A imagem deve ser salva como PNG.
- Crescimento considerável no tamanho do arquivo.

### 🔹 Versão 3 – Simulação com Arquivo SFX (AutoExtraível)

> Engenharia social combinada com esteganografia: um `.exe` abre um PDF real, mas também executa um script oculto.

```
📦 Conteúdo embutido:
  ├── documento.pdf       # visível ao usuário
  └── script_oculto.exe   # executado em segundo plano
```

### 🔹 Versão 4 – Codificação com Ave Maria de Trithemius + Esteganografia

Essa versão aplica a técnica histórica de Trithemius, onde cada letra do alfabeto é substituída por uma **frase religiosa** padronizada. Esse método era utilizado como forma de disfarçar mensagens ocultas com aparência devocional.

A mensagem final pode ser visualmente interpretada como um texto litúrgico comum, mas na verdade esconde **informações alfabéticas codificadas**.

#### Funcionamento

- Cada letra (de A a Y) é substituída por uma frase.
- Espaços entre palavras se tornam quebras de linha (`\n`), simulando estrutura de verso.
- Não há codificação para a letra `Z` por omissão histórica.

#### Dicionário Utilizado

```python
trithemius_dict = {
    'A': "no céu", 'B': "para todo o sempre", 'C': "um mundo sem fim",
    'D': "numa infinidade", 'E': "perpetuamente", 'F': "por toda a eternidade",
    'G': "durável", 'H': "incessantemente", 'I': "irrevogavelmente",
    'J': "irrevogavelmente", 'K': "eternamente", 'L': "na sua glória",
    'M': "na sua luz", 'N': "no paraíso", 'O': "hoje", 'P': "na sua divindade",
    'Q': "em Deus", 'R': "na sua felicidade", 'S': "no seu reino",
    'T': "na sua majestade", 'U': "na sua beatitude", 'V': "na sua beatitude",
    'W': "na sua beatitude", 'X': "na sua magnífica", 'Y': "ao trono"
}
```

#### Exemplo de Codificação

Mensagem original:
```
Mensagem Secreta
```

Resultado codificado:
```
na sua luz perpetuamente no paraíso na sua felicidade perpetuamente
no seu reino perpetuamente um mundo sem fim perpetuamente na sua majestade perpetuamente no céu
```

#### Código Principal

```python
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
```

## ✅ Conclusão

Este projeto mostra como técnicas de esteganografia podem ser aplicadas de formas diversas — seja em nível de bits, metadados, ou até através da engenharia social e códigos disfarçados.
