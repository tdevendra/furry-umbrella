# furry-umbrella
    Spark Pipelines Examples

    1- Added Sales example for products

     Output:
     sales.py: Sales per product

[(1, 92), (2, 1), (4, 23), (7, 21), (9, 39), (10, 61), (11, 168)]

     regionsales.py: Region wise product total sales

{u'Canada': [(11, 14), (7, 20)], u'Israel': [(9, 27)], u'SAfrica': [(1, 32)], u'Singapore': [(10, 20)], u'Switz': [(10, 4)], u'Finland': [(11, 22)], u'India': [(4, 2), (9, 11), (1, 19), (2, 1), (10, 2)], u'SKorea': [(10, 2)], u'US': [(4, 7), (1, 21), (9, 3), (11, 12), (7, 1)], u'Malaysia': [(10, 11)], u'China': [(1, 20)], u'Germany': [(4, 14), (11, 120)], u'Russia': [(10, 22)]}


    2- Added Sample plotting for sales using matplotlib, to be run using jupyter ipython notebook

    3- Running wordcount.py example using kafka
    
    wordcount.py

    'test' is topic name of kafka.

    [@sandbox kafka_2.11-0.10.1.0]$ bin/kafka-topics.sh --describe --zookeeper 0.0.0.0:2181 --topic test

    Topic:test      PartitionCount:1        ReplicationFactor:1     Configs:

        Topic: test     Partition: 0    Leader: 0       Replicas: 0     Isr: 0

    [@sandbox kafka_2.11-0.10.1.0]$



4- Log Analyzer with spark 

ml/log_analyzer.py
