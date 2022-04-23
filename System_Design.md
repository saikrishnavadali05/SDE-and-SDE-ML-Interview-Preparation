### Tushar Roy (Introduction to System Design)

### Video 1 : https://www.youtube.com/watch?v=UzLMhqg3_Wc

> ABCD of System Design
* A - Always ask good questions
* B - Buzz Words NO NO NO (Don't use words without proper knowledge or which you found out by quick researching for 10 minutes the previous day) 
* C - Clear and Organized Thinking
* D - Drive Discussions (80 myself - 20 interviewr should speak Rule)

> Things to consider
1. Features
2. API
3. Availability
4. Latency
5. Scalability
6. Durability
7. Class Diagram
8. Security and Privacy
9. Cost-effective

> Must know concepts for System Design Questions
1. CAP Theory -> Consistency - Availability - Partition Tolerance
   * Difference between SQL and NoSQL Databases (Which Database chooses what? over the above 3 (CAP))?
2. Vertical Scaling (Increasing System Resources like Memory RAM, etc) or Horizontal Scaling (Increasing Number of Hosts - Making Distributed System)
3. acid vs base database
4. Partitioning or Sharding of Data (What is Consistent Hashing)
5. Optimisstic Vs Pessimistic Locking in databases
6. Strong vs Eventual Consistency
7. Relational DB (follows ACID) vs NoSQL
8. Types of NoSQL Databases
  * Key-Value Pair
  * Wide Column
  * Document based
  * Graph Based
9. Caching 
10. Data Centers, Racks and Hosts
11. CPU, Memory, Harddrive, Network Bandwidth
12. Random vs Sequential Read/Write on Disk
13. Http / Https vs WebSockets
14. TCP / IP Model
15. IPV4 vs IPV6
16. TCP vs UDP
17. DNS Look up
18. Https and TLS
19. Public Key Infrastructure & Certificate Authority
20. Symmetric vs Asymmetric Key
21. Load Balancer - L4 vs L7
22. CDNs and Edge
23. Bloom Filters and Count Min Sketch
24. Paxos - Consensus over Distributed hosts, Leader Election
25. Design Patterns and Object Oriented Design
26. Virtual Machines and Containers
27. Publisher Subscriber or Queue
28. Map Reduce
29. Multi threading, concurrency, locks and synchronization, CAS (Compare and Swap) 

> Some of the Tools that have implemented the above concepts

1. Cassandra - 22:50 
2. MongoDB/Couchbase - 23:22 
3. Mysql - 22:36 
4. Memcached - 23:52
5. Redis - 23:52 
6. Zookeeper - 24:30 
7. Kafka - 25:00 
8. NGINX - 25:17 
9. HAProxy -  25:17 
10. Solr, Elastic search - 25:32 
11. Amazon S3 - 25:45 
12. Docker, Kubernetes, Mesos - 26:00 
13. Hadoop/Spark and HDFS - 26:17

## References
https://docs.datastax.com/en/cassandr...
http://cloudurable.com/blog/kafka-arc...
https://zookeeper.apache.org/doc/trun...
http://www.allthingsdistributed.com/f...
https://research.google.com/archive/b...
https://en.wikipedia.org/wiki/CAP_the...
https://en.wikipedia.org/wiki/Consist...
https://www.mongodb.com/mongodb-archi...
https://en.wikipedia.org/wiki/HTTP/2
https://en.wikipedia.org/wiki/Transpo...


### Video 3
### Design messaging/chat service like Facebook Messenger or Whatsapp
### Link : https://www.youtube.com/watch?v=zKPNUMkwOJE&list=PLrmLmBdmIlps7GJJWW9I7N0P0rB0C3eY2&index=3

1. **Facebook** - Text messages within the chat are not encrypted
2. **Whatsapp / Signal** - Text messages within the chat are encrypted. (Even company cannot read it).
3. **Cassandra DB** - Cassandra is a free and open-source, distributed, wide-column store, NoSQL database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.
4. **Redis DB (For Distributed Cache)** - What is Redis database? What is Redis? Redis, which stands for Remote Dictionary Server, is a fast, open source, in-memory, key-value data store. Redis is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine. Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams.
5. **WebSocket** - is a bidirectional communication protocol that can send the data from the client to the server or from the server to the client by reusing the established connection channel. The connection is kept alive until terminated by either the client or the server.
6. **HTTP** - it is unidirectional (request -> response type). Server cannot initiate a communication by itself. In our scenario it is not helpful
7. 3 users, 3 servers, load balancer, various tables within the database.
