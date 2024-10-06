from opensearchpy import OpenSearch

# Conectar ao OpenSearch
host = 'localhost'  # Endereço do servidor OpenSearch
port = 5601          # Porta padrão
auth = ('admin', 'MyS3cure@Password!')  # Autenticação

client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_auth=auth,
    use_ssl=True,  # Habilitar HTTPS
    verify_certs=False,  # Desativa a verificação de certificados (use com cautela)
    timeout=40
)

# Realizar uma consulta limitando o resultado a 1 documento
response = client.search(
    body={
        "query": {
            "match_all": {}
        }
    },
    index="nome_do_indice",  # Substitua pelo nome do seu índice
    size=1  # Limita a 1 resultado
)

# Acessar e imprimir os resultados
if response['hits']['hits']:
    document = response['hits']['hits'][0]  # Primeiro documento encontrado
    print(document)
else:
    print("Nenhum documento encontrado.")