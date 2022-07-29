## Create a AWS RDS and reboot RDS using boto3.

#### Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks. You can follow this [link](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) to know more.

#### This template can be use to create AWS RDS and how we can reboot the RDS usinb boto3

-------------

**Files:** 
```
    create_rds.py
    reboot_rds.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to create the RDS or Reboot the RDS.

        python3 create_rds.py
        python3 reboot_rds.py
