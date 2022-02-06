from config import PAIS
from helpers import top_noticias
if __name__ =='__main__':
    noticias = top_noticias(PAIS)

print(f"***Listando as Top notícias do  {PAIS.upper()} ***")
for numero in range(len(noticias)):
    print(f"{numero + 1} - {noticias[numero]}")




