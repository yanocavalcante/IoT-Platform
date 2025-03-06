# IoT Platform

Repositório introdutório sobre a utilização da Plataforma para <em>Internet</em> das Coisas desenvolvida pelo Laboratório de Integração <em>Software-Hardware</em> (LISHA) da Universidade Federal de Santa Catarina (UFSC).

# Pré-requisitos

Antes de tentar utilizar diretamente quaisquer códigos desse repositório é imprescindível:

- Credenciais de acesso à LISHA's IoT Platform.
- Instalaçãos dos pacotes definidos em requirements.txt.

# SmartData

O conceito de SmartData utilizado pela plataforma do LISHA requer uma manipulação mais cuidadosa dos dados inseridos.
Inicialmente, deve-se ter uma série que comporte e satisfaça o espaço ocupado por esses dados, na criação da série,
um modelo básico de série está disposto abaixo, em formato JSON:
```JSON
{"series": {
    "version": "1.2" ,
    "unit": 2224441636, 
    "x": 3746950,
    "y": -4230498,
    "z": -2947091,
    "r": 999999,
    "t0": 1741283792000000,
    "tf": 2056816592000000,
    "dev": 1,
    "signature": "BL0001"}
}
```
Esse exemplo representa uma série responsável por abstrair um dispositivo (uma boia) identificado como "BL0001", o ponto central da série é definido pelos pontos "x", "y" e "z", definidos em <em>Earth Centered Earth Fixed</em> (ECEF). A série criada engloba todos os pontos que:

- Têm os mesmos identificadores "signature" e "dev".
- Utilizam a mesma unidade definida por "unit".
- Estão dentro do raio definido por "r" a partir do ponto central.
- Estão dentro do espaço temporal definido por "t0" e "tf".

Para entender melhor o conceito de SmartData, consulte: <a href="https://epos.lisha.ufsc.br/IoT+Platform">Lisha - IoT Platform Docs</a>.


## Observações
<p style="text-align: center;"><em>O ideal é definir coordenadas iniciais relativamente próximas do ponto onde as boias serão lançadas e um raio grande, para evitar que durante a deriva as boias se desloquem para fora do raio definido.</em></p>

<p style="text-align: center;"><em>No contexto de utilização do Laboratório de Engenharia e Ciências Oceânicas, cada boia oceânica deve ser associada a uma "signature" específica e única, de preferência, seguindo um padrão previamente estabelecido.</em></p>

<p style="text-align: center;"><em>Já o "dev" deve referenciar um dispositivo específico da boia, em outras palavras, um sensor. É lógico pensar que uma boia pode conter mais de um sensor, e por consequência, cada um deve contar com unidades de medidas diferentes.</em></p>

# Utilização

A seguir, uma descrição breve sobre a utilização da Plataforma para os seus 3 principais casos de uso, criação de séries, inserção de dados e recuperação deles, indicando os arquivos .py onde cada deles é aplicado.

## Criação de Séries

O primeiro passo é a criação de uma série onde os <em>datapoints</em> serão inseridos. Um exemplo de criação de série pode ser encontrado no arquivo ./basics/create_series.py.

## Inserção de Dados

Após a criação de uma série já podemos criar os <em>datapoints</em> que serão alocados para essa série. E de maneira semelhante a criação da série devemos apontar um mínimo de "atributos" para que os <em>datapoints</em> sejam criados corretamente. 

Um exemplo de criação de <em>datapoints</em> pode ser encontrado no arquivo ./spotter_data/put_spotter.py. Nele, esses pontos foram criados tendo como base um arquivo .csv (Comma Separated Values) que contém dados de um experimento realizado com uma boia da <em>Sofar Ocean</em>.

## Recuperação de Dados

Agora, com uma série criada e com dados inseridos dentro dela, podemos partir para a recuperação deles. Um exemplo de como fazer isso pode ser encontrado no arquivo ./basics/get_data.py.

Para entender melhor a utilização dos <em>endpoints</em> fornecidos pela API da <em>IoT Platform</em> consulte o <em>Swagger</em> suportado pela Superintendência de Governança Eletrônica e Tecnologia da Informação e Comunicação (SeTIC) da UFSC: <a href="https://iot.ufsc.br">https://iot.ufsc.br</a> 

# Sensores - "Devices"
Tabela indicando o código interno dos sensores, as unidades de medida, as suas abstrações e a sua codificação hexadecimal feita pela <em>IoT Platform</em>.

<img src="images/sensors.png">
<p style="text-align: center;"><em>A plataforma ainda não possui suporte para a utilização de "Graus", por isso foi utilizado "Ratio" como substituto.</em></p>
