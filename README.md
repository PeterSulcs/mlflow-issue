## Reproducing MLFlow artifact store SSL error

This repo contains a simple docker-compose setup to illustrate the error with self signed certificates for the s3 store with versions of MLFlow later than 1.11.0.

## Steps to reproduce the error

```
git clone 
docker-compose up


```

locally, with a Python 3.7.9 environment:
```
source .env
python mlflow_test.py
```
