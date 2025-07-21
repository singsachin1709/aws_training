import boto3

# Create EC2 resource
myec2 = boto3.resource('ec2', region_name='ap-south-1')  # Replace with your desired region

# Launch EC2 instance
response = myec2.create_instances(
    ImageId='ami-0a1235697f4afa8a4',  # Amazon Linux 2 AMI for us-east-1
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
)

print(f"Launched instance with ID: {response[0].id}")
