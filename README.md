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
