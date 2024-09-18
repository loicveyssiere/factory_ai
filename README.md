

```
docker compose exec kong kong migrations bootstrap
docker-compose restart kong


docker pull kong/deck
docker run --rm -v $(pwd)/kong.yml:/tmp/kong.yml --network="host" kong/deck:latest sync --state /tmp/kong.yml
```
