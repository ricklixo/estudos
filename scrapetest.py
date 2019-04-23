import requests
from bs4 import BeautifulSoup

#atribui a variável r o site informado
r = requests.get('http://serious.gameclassification.com/EN/games/index.html?start=0&display=table')

soup = BeautifulSoup(r.text, 'html.parser')

#o beautiful soup pega todos os 'a' class que possuem os atributos "title = "view details""
results = soup.find_all('a', attrs={'title':'view details'})

#imprime na tela o tamanho dos resultados
print(len(results))

#imprime os 3 primeiros resultados, indo de 0 a 3.
#print(results[0:3])

#atribui o primeiro resultado à variável first_result
first_result = results[0]
print(first_result)

#localiza a string "strong" no primeiro resultado.
x = first_result.find('class')
print(x)

