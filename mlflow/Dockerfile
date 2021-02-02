FROM python:3.7-slim-buster
# Install python packages
RUN pip install mlflow==1.13.1 boto3 pymysql

# install the cert for minio:
ADD public.crt /usr/local/share/ca-certificates/minio.crt
RUN chmod 644 /usr/local/share/ca-certificates/minio.crt && update-ca-certificates

# install the cert for botocore and certifi
ADD public.crt /usr/local/lib/python3.7/site-packages/botocore/cacert.pem
ADD public.crt /usr/local/lib/python3.7/site-packages/certifi/cacert.pem

