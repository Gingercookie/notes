# Module 2 - Storage

## AWS S3
Like all AWS products, S3 is a set of APIs that you can use to interface with.

S3 is object-level storage, meaning when a file is changed, that file must be uploaded again to persist.
The only operations you can do to a file on S3 are read and delete the file. Nothing else. This means it is WORM = write once, read many.

You are allowed to stored as much data as you want (unlimited number of files), but no individual object can be larger than 5TB. The largest HTTP POST you can do is 5GB.

By default, with no additional configuration, this is a super high-availability service. Nobody will lose data here on accident.

By default, all content uploaded to an S3 bucket is private. Only the resource owner can access any of it.

#### Use-Cases
- Storing and Distributing static web content
- Host entire static websites
- Data-store for computation and large-scale analytics
- Backup tool for data centers
```
https://se-ap-northeast-1.amazonaws.com/[bucket name]
https://se-ap-northeast-1.amazonaws.com/[bucket name]/Preview2.mp4
```

#### Access Control
```
{
    "Version": "2012-10-17",
    "Id": "Policy1231512312",
    "Statement": [
        {
            "Sid": "Access-to-specific-VPCE-only",
            "Effect": "Deny",
            "Action": "s3:*",
            "Resource": ["arn:aws:s3:::examplebucket",
            "arn:aws:s3:::examplebucket/*"],
            "Condition": {
                "StringNotEquals": {
                    "aws:sourceVpce": "vpce-1a2co23"
                }
            },
            "Principal": "*"
        }
    ]
}
```

#### Versioning
By default, versioning is turned off. This is primarily to save money. If you were to version large files, then you are storing multiple copies of that same large file.

#### Uploading
- CLI
- AWS Console
- APIs
- SFTP
- AWS DataSync
- S3 Multi-part upload. Better recovery for network errors and large files

#### Cost
Pay for what you use..
- GB per month
- Transfer OUT to other regions, or to the internet
- PUT, COPY, POST, LIST, and GET requests (per 1,000 or something)

Don't pay for
- Transfer IN to S3
- Transfer OUT to EC2 in the same region or to CloudFront

## AWS Glacier
Glacier is a special storage class of S3. It's meant for use with long-term data storage, archive/backup, and is very low-cost storage.

Vaults are the containers used in Glacier. When you create a vault, you specify the AWS Region and vault name. Each object uploaded to a vault is called an "archive". Each archive has a unique ID (to that region) and an optional description.

#### Retrieval
- Expedited Retrieval - 1-5 minutes to retrieve but rate of $0.03/GB
- Standard - 3-5 hours for data
- Bulk - 5-12 hours, but the rate of $0.0025/GB

#### Storage comparison
- S3 Standard - High-availability, frequently accessed objects
- S3 Standard Infrequently Accessed (IA) - lower cost per GB, higher cost for retrieval
- S3 One-Zone IA - Cost even less, but no replication
- S3 Glacier - Dirt cheap, but low availability

#### Lifecycle Policies
You can define lifecycle policies to move your data to a different storage class based on age only. I.e. move data to S3 IA after 3 months, move to glacier after 1 year, etc...

You can only create policies based on absolute object age, however.

#### Regional Considerations
Your data will be governed and must be compliant to the laws based on the region where the data is stored.

The cost of the data may even be more based on the region, if there is a specific tax that applies in that region.
