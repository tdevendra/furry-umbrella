# furry-umbrella
Spark Pipelines Examples

1. Added Sales example for products

Execute from dir such as project-git with checkout as below

sudo /usr/hdp/2.4.0.0-169/spark-2.0.1-bin-hadoop2.4/bin/spark-submit --master local[4] project-git/ml/sales.py project-git/data/sales_per_day.txt


Output:
[(1, 92), (2, 1), (4, 23), (7, 21), (9, 39), (10, 61), (11, 168)]

Plotting to be added
