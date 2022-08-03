# import the boto3 which will use to interact  with the aws
import boto3

# We will take the all imput from the end user.

# You need to enter rds as input
AWS_service= input("Enter the service name\n")

# you can enter the instance type for your RDS instance
instance_class=input("Enter the instance class\n")

database_name=input("Enter the database name\n")

# You need to enter the engine name like - MySQL
engine_name=input("Enter the Engine name\n")

# user name and password
user_name=input("Enter the user name\n")
user_password=input("Enter the password\n")



client = boto3.client(AWS_service)

create_rds = client.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass=instance_class,
    DBInstanceIdentifier= database_name,
    Engine= engine_name,
    MasterUserPassword= user_password,
    MasterUsername= user_name
)

print(create_rds)

print("Your RDS has been created Successfully ")