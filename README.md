# exchange-optimizator

Codigo para prueba de buda.com

## Arquitectura y estructura de clases
![Arquitectura](https://raw.githubusercontent.com/tuto/exchange-optimizator/main/doc/architectura.png)
- bussiness: 
    Capa de negocio

    1. ExchangeList: lista de exchanges
    2. Exchange: Clase que representa un exchange

- domain: 
    Objetos de dominio

    1. ExchangeInterface: Interfaz que define una clase de exchange, para poder crear nuevos exchanges
    2. MarketId: Objeto de dominio que representa un mercado

- infrastructure: 
    Capa de anticorrupción donde los clientes se conectan a los exchanges y devuelven objetos de dominio

    1. Rates: Clase que representa un cliente para sacar los rates
    2. Buda: Cliente para conectarse a buda
    3. Bitstamp: Cliente para conectarse a bitstamp

## Ejecución

Para ejecutar el programa se puede utilizar un runner que se creó. 
```
python3 runner.py -m btc-clp -q 100000 -r 0.01
```
- -m: mercado
- -q: cantidad de clp a obtener
- -r: cargo por cambio a usd


## Tests
Para correr los tests se necesita tener instalado el modulo **coverage** de python y ejecutar
```
coverage run --source=src/ -m unittest discover ; coverage report -m
......
----------------------------------------------------------------------
Ran 6 tests in 0.006s

OK
Name                                     Stmts   Miss  Cover   Missing
----------------------------------------------------------------------
src/bussiness/exchange.py                   23      0   100%
src/domain/exceptions.py                     4      0   100%
src/domain/exchangeInterface.py              0      0   100%
src/domain/marketid.py                       8      0   100%
src/domain/ticker.py                         9      0   100%
src/infrastructure/clients/bitstamp.py      18      8    56%   42-49
src/infrastructure/clients/buda.py          18      8    56%   42-49
src/infrastructure/clients/rates.py         16      8    50%   33-40
----------------------------------------------------------------------
TOTAL                                       96     24    75%
```


## Como agregar un nuevo exchange?

Para crear un nuevo exchange solo se debe crear una nueva configuración en exchange-config.yaml y crear una nueva clase en infrastructure/clients 