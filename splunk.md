# Splunk

### Indexing Overview

[Link](http://docs.splunk.com/Documentation/Splunk/6.6.2/Indexer/Aboutindexesandindexers) to official documentation.

- _Indexing_ - transforming data into splunk events
- _Index_ - a data repository which holds indexed events
- _Indexer_ - the enterprise component which performs indexing
- _Indexer Cluster_ - a set of mirrored indexers to increase availability


_Indexing_ refers to transforming incoming data into splunk events. These events
are stored in _Indexes_, which are data repositories created and managed by
Splunk Enterprise components. An _Indexer_ is the name of the enterprise
component that performs the indexing. In a small environment, the indexer is
often performing other duties as well, such as data input or search management.
In a large environment, an indexer cluster is typically used. This allows
multiple simultaneous searches and provides data loss prevention

##### Indexes
Two kinds of files are created when indexing occurs
1. Raw, compressed log data
2. Indexes that point to the raw data, plus some metadata. This is the types
of individual, searchable events are saved, as well as timestamps, and other
user-defined fields, etc.

##### Indexers

There are two main jobs of the indexer. Indexing the incoming data, and
searching the data that it has indexed.
