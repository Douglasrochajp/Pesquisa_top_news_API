import requests
from config import URL_BASE_TOP_HEADLINES,PAIS,CHAVE_API

def top_noticias(pais):
    """Retorna noticias do site newsapi.org
    :param pais: inserir pais para pesquisa
    :return: lista de noticas do pais
    """
    url = f"{URL_BASE_TOP_HEADLINES}country={PAIS}&apikey={CHAVE_API}"
    #Coletando dados em Json
    resposta = requests.get(url).json()
    #print(resposta)

    #Abrir resultado num nagegador, site ONLINE JSON VIWER
    #Pegando todos os artigos

    artigos = resposta['articles']
    #print(artigos)

    #Lista vazia para inserir noticias
    noticias = []

    for artigo in artigos:
        noticias.append(f"{artigo['title']},"
                        f"Imagem {artigo['urlToImage']},"
                        f"Publicado em: {artigo['publishedAt']}")
        #print(noticias)
    return noticias
