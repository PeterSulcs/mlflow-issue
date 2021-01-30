FROM python:3.7-slim-buster
# Install python packages
RUN pip install mlflow boto3 pymysql

# install the cert for minio:
ADD public.crt /usr/local/share/ca-certificates/minio.crt
RUN chmod 644 /usr/local/share/ca-certificates/minio.crt && update-ca-certificates
