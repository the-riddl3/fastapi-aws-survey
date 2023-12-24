import os
import boto3

# credentials


# Create an S3 client
s3 = boto3.client('s3',
                  aws_access_key_id='AKIA2RRJTY3AGI7FBO3X',
                  aws_secret_access_key='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',
                  region_name='eu-central-1'
                  )

# Specify the file to upload
filename = 'data/survey_cu.csv'
bucket_name = 'surveycu'
destination_filename = 'survey_cu.csv'

# Upload the file
s3.upload_file(filename, bucket_name, destination_filename)

# clear data
os.remove('data/survey_cu.csv')

print("upload complete!")
