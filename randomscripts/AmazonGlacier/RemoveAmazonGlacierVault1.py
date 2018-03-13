#import boto3

#glacier = boto3.resource('glacier')
#account = glacier.Account('645504553392')

import boto3

client = boto3.client('glacier')

'''
#Delete vault
glacier = boto3.resource('glacier')
vault = glacier.Vault('645504553392','NasPhotos')
vault.delete()
'''
'''
#output the job listing for a vault
response = client.list_jobs(vaultName='NasPhotos')
print(response)
'''

'''
NasPhotos Job Ids:
1FqKWmf_9WQUcw-xlewc0RzECeRsEVm4v3ZDXPEGbbleDPwGUTC802YjGIuNWSRXc9_LqIdL0TY_PC8rERQCU83uTG2S

duwlcgp4g3py1RfCXxYnMhf4SPQJar61l-xv18Pr_qGcxKanMuFg6qLHr_3GnSCgkwu7xHnTsRbr8djCq86bWG6YHg_9

a0ofvV_wx-SIe3l9A9aUDBfdLCAk3Y4_pvjgU-dikHnzHJw5lWvgFFuBg0Bz6nCOxkl3wO7WumXZ92UOWBuEfAtHt0ST

i_RBlMOfEM4l4voEpHLgycF58GDLN84JSImdaZWjaQscF1MWtw4AgyyLiwc_z3VoVFmcDuizNPZJxMx8kd2fL7odkUK0
'''

#remove archive files

'''
import boto3
glacier = boto3.resource('glacier')
archive = glacier.Archive('645504553392','NasPhotos','i_RBlMOfEM4l4voEpHLgycF58GDLN84JSImdaZWjaQscF1MWtw4AgyyLiwc_z3VoVFmcDuizNPZJxMx8kd2fL7odkUK0')

response = archive.delete()
'''
