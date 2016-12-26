# furry-umbrella
Spark Pipelines Examples

1. Added Sales example for products

Execute from dir such as project-git with checkout as below

sudo /usr/hdp/2.4.0.0-169/spark-2.0.1-bin-hadoop2.4/bin/spark-submit --master local[4] project-git/ml/sales.py project-git/data/sales_per_day.txt


Output:
sales.py: Sales per product

[(1, 92), (2, 1), (4, 23), (7, 21), (9, 39), (10, 61), (11, 168)]

regionsales.py: Region wise product total sales

{u'Canada': [(11, 14), (7, 20)], u'Israel': [(9, 27)], u'SAfrica': [(1, 32)], u'Singapore': [(10, 20)], u'Switz': [(10, 4)], u'Finland': [(11, 22)], u'India': [(4, 2), (9, 11), (1, 19), (2, 1), (10, 2)], u'SKorea': [(10, 2)], u'US': [(4, 7), (1, 21), (9, 3), (11, 12), (7, 1)], u'Malaysia': [(10, 11)], u'China': [(1, 20)], u'Germany': [(4, 14), (11, 120)], u'Russia': [(10, 22)]}


2. Added Sample plotting for sales using matplotlib, to be run using jupyter ipython notebook

3. Running wordcount.py example using kafka

sudo /usr/hdp/2.4.0.0-169/spark-2.0.1-bin-hadoop2.4/bin/spark-submit --master local[4] --packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.0.1,org.apache.spark:spark-streaming-kafka-0-8_2.10:2.0.1 --driver-class-path spark-streaming-kafka-0-8_2.10-2.0.1.jar,spark-streaming-kafka-0-8-assembly_2.11-2.0.1.jar --jars spark-streaming-kafka-0-8_2.10-2.0.1.jar,spark-streaming-kafka-0-8-assembly_2.11-2.0.1.jar --conf "spark.dynamicAllocation.enabled=false" wordcount.py 0.0.0.0:2181 test


