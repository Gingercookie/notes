# Module 4 - Databases

## Types of DBs

#### Relational
- Microsoft SQL Server
- Oracle DB
- MySQL

Data is stores in rows and columns separate the attributes for each object in each row. The database columns (schema) must be locked before entering data. The schema may be changed if the DB is taken offline, and this will alter the entire database.

Data is queried used SQL statements.

These databases scale vertically by adding power.

#### Non-Relational
- MongoDB
- Cassandra
- Redis

NoSQL databases can store data using many storage models, including key-value pairs, documents, and graphs. Schemas are dynamic. Rows don't have to contain data for each column. Data is generally queried by focusing on collections of documents.

These databases scale horizontally by adding more servers.

## AWS Database Options

#### Unmanaged Databases
This is when you deploy a database to an EC2 instance. In that case, you still have to account for availablity, backups, OS patches, scaling, etc.

#### Managed Databases
This is when you used an AWS managed database service. In this case, the only thing you have to manage is your App Optimization.

#### Relational
- Amazon RDS (focus)
    - Fully managed RDBS
    - Provisions new instances in a few minutes
    - Scales vertically with only a few clicks
- Amazon Redshift

#### Non-Relational
- Amazon DynamoDB (focus)
    - Fully managed Non-Relational DB
    - Event-driven programming (serveless computing)
    - Extreme horizontal scaling
    - millisecond latency
- Amazon ElastiCache
- Amazon Neptune

## DB Security
- AES-256 encryption when enabled
- TLS for connecting to the DB
- Event notifications - shutdown, failover, security group changed, etc..

## Migration
There are a couple AWS DB migration tools you can use to get onto their platform and start using their DBs
