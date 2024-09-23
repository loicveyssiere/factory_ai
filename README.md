# Securing Ollama for LLM as a service

In this small project, we test two ways to protect an Ollama server. Ollama does
not have a security mechanism, so it is impossible to expose it as a
network-accessible service. A simple solution involves creating a proxy using
Nginx `reverse_proxy`. For more features like user tracking and rate limiting the
amount of data exchanged in megabytes, we propose an API gateway using Kong
`api_gateway`.

## Access through Reverse Proxy (Nginx)

```
cd reverse_proxy
docker compose up -d
```

## Access through API Manager (Kong)

```
cd api_gateway
docker compose up -d
```
