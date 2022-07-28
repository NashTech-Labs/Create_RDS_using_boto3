# import the boto3 which will use to interact  with the aws
import boto3

client = boto3.client('rds')
DBInstanceIdentifier=input("Enter the database name")
response = client.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass=input("Enter the instance class"),
    DBInstanceIdentifier=input("Enter the database name"),
    Engine='MySQL',
    MasterUserPassword=input("Enter the password"),
    MasterUsername=input("Enter the user name"),
)

print(response)