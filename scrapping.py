import requests #Responável por enviar a requisição 
from bs4 import BeautifulSoup # Resposável por tratar a requisição 

# class -> feed-post-link 

#URL so Site 
url = "https://www.cnnbrasil.com.br/tudo-sobre/mercado-financeiro/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Wind; x64) AppleWebkit/537.36" # (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
}


# Fazendo a requisição HTTP 
resposta = requests.get(url, headers=headers)

# Verificar se deu certo 
if resposta.status_code == 200:
    # código 200 -> Sucesso 
    print("Requisição feita com sucesso.")
    # print(resposta.text) # retorno 
    # preenchendo nossa sopa
    soup = BeautifulSoup(resposta.text, "html.parser")
    # encontrando as noticias 
    noticias = soup.find_all("a", class_="home__list__tag" )
    
    print("Últimas noticias do g1:")
    for index, noticia in enumerate(noticias):
        print(f"{index + 1}. {noticia.text.strip()} - {noticia['href']}")
        
        
        
        
        
    