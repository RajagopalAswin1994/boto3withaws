# import boto.ec2
# conn = boto.ec2.connect_to_region("us-east-1",
# aws_access_key_id='AKIAVJ26OEHB7TASS7U4',
# aws_secret_access_key='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')
# conn = boto.ec2.connect_to_region("us-east-1")
# conn.run_instances(ImageId = 'ami-0cff7528ff583bf9a',
#         key_name='practice-vm-lat',
#         instance_type='t2.micro',
#         security_groups=['default'])


from pydoc import cli
import boto3
client = boto3.client('ec2',region_name='us-east-1')
resp = client.run_instances(ImageId = 'ami-0cff7528ff583bf9a (64-bit (x86))',
                            instanceType  ='t2.micro',
                            MinCount=1,
                            MaxCount=1)
for instance in resp['instances']:
    print(instance['InstanceId'])