# from: https://github.com/SeanPLeary/mlflow-minio-h2o-example/blob/master/minio_create_bucket.ipynb

from minio import Minio
import json
import os



minioClient = Minio(os.environ['MLFLOW_S3_ENDPOINT_URL'].split('//')[1],
                  access_key=os.environ['AWS_ACCESS_KEY_ID'],
                  secret_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                  secure=True)

print(minioClient.list_buckets())


minioClient.make_bucket('mlflow')




buckets = minioClient.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)



policy = {"Version":"2020-01-29",
        "Statement":[
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:GetBucketLocation",
            "Resource":"arn:aws:s3:::mlflow"
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:ListBucket",
            "Resource":"arn:aws:s3:::mlflow"
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:GetObject",
            "Resource":"arn:aws:s3:::mlflow/*"
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:PutObject",
            "Resource":"arn:aws:s3:::mlflow/*"
            }

        ]}

minioClient.set_bucket_policy('mlflow', json.dumps(policy))

# List all object paths in bucket that begin with my-prefixname.
objects = minioClient.list_objects('mlflow', prefix='my',
                              recursive=True)
for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
          obj.etag, obj.size, obj.content_type)
