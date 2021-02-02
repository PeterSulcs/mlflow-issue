## Reproducing MLFlow artifact store SSL error

This repo contains a simple docker-compose setup to illustrate the error with self signed certificates for the s3 store with versions of MLFlow later than 1.11.0.

## Steps to reproduce the error

```
git clone https://github.com/PeterSulcs/mlflow-issue.git
cd mlflow-issue
docker-compose up
```


Then, locally, with a Python 3.7.9 environment:
```
pip install mlflow==1.13.1 boto3 scikit-learn
source .env
python mlflow_test.py
```

Expected result is:
```
❯ python train.py
Score: 0.6666666666666666

[very long stacktrace]

botocore.exceptions.SSLError: SSL validation failed for https://127.0.0.1:9000/mlflow/1/a52d109b31cb4effa8364bd1a10cdaf2/artifacts/model/model.pkl [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1091)
```

## Steps to resolve

```
unset REQUESTS_CA_BUNDLE
pip install mlflow==1.11.0
source .env
python mlflow_test.py
```

Expected result is:
```
❯ python train.py
Score: 0.6666666666666666
Model saved in run a9c1470d81714a1d880b47ea64477afa
```

The artifacts can be viewed in the [MLFlow UI](http://127.0.0.1:5000) or [Minio UI](https://127.0.0.1:9000)
