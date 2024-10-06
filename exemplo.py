from opensearchpy import OpenSearch
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Ignorar avisos de certificado não verificado
warnings.filterwarnings('ignore', category=InsecureRequestWarning)

# Configurações de conexão
host = 'localhost'
port = 9200
auth = ('admin', 'MyS3cure@Password!')

# Criação do cliente
client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False
)

index_name = 'contato'  # O nome do seu índice

def filtrar_aniversarios_por_dia_mes(client, dia, mes):
    response = client.search(
        index='contato',
        body={
            'query': {
                'script': {
                    'script': {
                        'source': """
                            doc['data_nascimento'].value.getDayOfMonth() == params.dia && 
                            doc['data_nascimento'].value.getMonthValue() == params.mes
                        """,
                        'params': {
                            'dia': dia,
                            'mes': mes
                        }
                    }
                }
            }
        }
    )
    
    for contato in response['hits']['hits']:
        nome = contato['_source']['name']
        email = contato['_source']['email']
        print(f"{nome} faz aniversário dia {dia}/{mes}. Mande uma mensagem para: {email}")

# Exemplo de uso
filtrar_aniversarios_por_dia_mes(client, 16, 7)