




## LIST
#print(python 'removeVault.py' eu-west-1 LIST)


#import boto3

#glacier = boto3.resource('glacier')
#vault = glacier.Vault('645504553392','NasPhotos')



from boto.glacier.layer1 import Layer1
from boto.glacier.vault import Vault
from boto.glacier.job import Job
import sys
import os.path
import json

access_key_id = "AKIAJYTRQUDKL3KNCBSA"
secret_key = "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"
target_vault_name = 'NasPhotos'

glacier_layer1 = Layer1(aws_access_key_id=access_key_id, aws_secret_access_key=secret_key)

print("operation starting...");

job_id = glacier_layer1.initiate_job(target_vault_name, {"Description":"inventory-job", "Type":"inventory-retrieval", "Format":"JSON"})

print("inventory job id: %s"%(job_id,));

print("Operation complete.")


response = glacier_layer1.list_jobs(
    vaultName='NasPhotos'
    )

#,
#limit='string',
#marker='string',
#statuscode='string',
#completed='string'

print(response)


aws glacier initiate-job --job-parameters '{"Type": "inventory-retrieval"}' --vault-name NasPhotos --account-id 645504553392 --region us-east-1


aws glacier initiate-job --account-id 645504553392 --vault-name NasPhotos --region us-east-1 --job-parameters '{"Type": "inventory-retrieval"}'


#remove vault
python .\removeVault.py us-east-1 NasDocuments
