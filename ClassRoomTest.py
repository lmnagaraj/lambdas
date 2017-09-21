
import boto3


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    kanna_raja = ec2.describe_instance_status()
    
    for instance in kanna_raja['InstanceStatuses']:
        if instance['InstanceId'] != 'i-045e61db5b2258cf2':
            ec2.start_instances(InstanceIds=['i-045e61db5b2258cf2'])
            print("rebooting i-045e61db5b2258cf2")
            break
