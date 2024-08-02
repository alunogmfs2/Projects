import requests
from random import randint
import os
import json
from PIL import Image, ImageFont, ImageDraw

def word_wrap(text, font, max_width):
    """Quebra o texto em várias linhas com base na largura máxima."""
    lines = []
    words = text.split()
    line = ""

    for word in words:
        # Adiciona a palavra atual à linha
        test_line = f"{line} {word}".strip()

        # Verifica se a linha excede a largura máxima
        bbox = font.getbbox(test_line)
        if bbox[2] - bbox[0] <= max_width:
            line = test_line
        else:
            # Se a linha excede, salva a linha atual e começa uma nova linha
            if line:
                lines.append(line)
            line = word

    if line:
        lines.append(line)

    return lines

# Definir o diretório onde as imagens estão localizadas
diretorio = 'E:\\Programacao\\Projetos\\Projects\\Python\\Meus_21_Projetos\\3_Estrela\\Gerador_Motivacional\\Imgs'

# Gerar um número aleatório para escolher a imagem
num_img = randint(1, 20)

def perguntar_API():
    category = 'failure'
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    response = requests.get(api_url, headers={'X-Api-Key': 'jImYjrz+uZ3PyYeEmjv9Ig==CEwLnbs8LTWIS2zf'})
    if response.status_code == requests.codes.ok:
        # Converter a resposta JSON em um dicionário
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

# Obter a resposta da API
resposta_API = perguntar_API()

# Verificar se a resposta da API foi obtida com sucesso
if resposta_API:
    # A API retorna uma lista de citações, então pegamos a primeira
    resposta_API = resposta_API[0]

    # Listar todos os arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Filtrar arquivos com base no número aleatório
    arquivos_filtrados = [a for a in arquivos if a.startswith(f'{num_img}')]

    # Verificar se há arquivos filtrados
    if arquivos_filtrados:
        # Construir o caminho do arquivo
        img_path = os.path.join(diretorio, arquivos_filtrados[0])

        # Abrir a imagem
        imagem = Image.open(img_path)

        # Redimensionar a imagem
        imagem_redimensionada = imagem.resize((800, 600))

        # Criar um objeto ImageDraw para adicionar texto
        imagem_d = ImageDraw.Draw(imagem_redimensionada)

        # Carregar a fonte com o tamanho especificado
        fonte = ImageFont.truetype("C:\\Windows\\Fonts\\ARIAL.TTF", 20)

        # Definir o texto a ser adicionado
        quote = resposta_API['quote']
        author = resposta_API['author']
        
        # Quebrar a citação em linhas
        largura_maxima = 750  # Ajuste conforme necessário
        linhas_citacao = word_wrap(quote, fonte, largura_maxima)

        # Adicionar a citação à imagem
        x, y = 50, 50
        espaco_entre_linhas = 10  # Espaço entre linhas

        # Cor do texto (cinza escuro)
        cor_texto = "#333333"  # Cor cinza escuro

        # Adicionar a citação linha por linha
        for linha in linhas_citacao:
            imagem_d.text((x, y), linha, font=fonte, fill=cor_texto)
            bbox = fonte.getbbox(linha)
            y += bbox[3] - bbox[1] + espaco_entre_linhas

        # Adicionar o nome do autor em uma nova linha
        y += 20  # Espaço extra antes do nome do autor
        imagem_d.text((x, y), f"- {author}", font=fonte, fill=cor_texto)

        # Salvar a imagem modificada
        imagem_redimensionada.save('imagem_editada.jpg')

        # Mostrar a imagem (opcional)
        imagem_redimensionada.show()
    else:
        print(f"Nenhum arquivo encontrado que comece com {num_img}")
else:
    print("Não foi possível obter a citação da API.")
