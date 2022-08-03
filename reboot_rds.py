# import the boto3 which will use to interact  with the aws
import boto3
# We will take the all imput from the end user.

# You need to enter rds as input
AWS_service= input("Enter the service name\n")

database_name=input("Enter the database name\n")

client = boto3.client(AWS_service)
reboot_rds = client.reboot_db_instance(
    DBInstanceIdentifier= database_name
)
print(reboot_rds)

print("Your RDS has been rebooted Successfully ")