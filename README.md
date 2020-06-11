# Combat API

## Development

Docker.

Use `aiohttp-devtools` for easier development.

Install `flake8` and respect its suggestions please.

## Using The API

### Request 

``` bash 
curl -X POST localhost:8000/v0/basic-combat -d '{"attacker": {"name": "London", "tokens": 9}, "defender": {"name": "Oxford", "tokens": 8}}'

```

### Response

``` bash
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 14
Date: Wed, 03 Jun 2020 12:40:32 GMT
Server: Python/3.8 aiohttp/3.6.2

{"result": -1}
```
