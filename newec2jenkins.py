import boto3
import sys

region=sys.argv[1]
access_key=sys.argv[2]
secret_key=sys.argv[3]

ec2 = boto3.resource('ec2',region_name=region,
	aws_access_key_id=access_key,
	aws_secret_access_key=secret_key)
	
instance = ec2.create_instances(
	ImageId='ami-0f7919c33c90f5b58',
	MinCount=1,
	MaxCount=1,
	KeyName='jumparun',
	SubnetId='subnet-0190a77b',
	InstanceType='t2.micro')
print(instance[0].id)