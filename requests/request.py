import requests

payload = {'key1': 'value1', 'key2': 'value2'} #passando parâmetros
r = requests.get("http://httpbin.org/get", params=payload)

url = 'https://api.github.com/some/endpoint'

r = requests.get(url)
print(r.text) #conteúdo da resposta
r.json() #respota json
r.status_code #código do status da resposta
r.headers #cabeçalho da resposta
