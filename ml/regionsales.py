"""
This is an example implementation of Region wise Sales Per Product 
Sample Usage:
bin/spark-submit ml/regionsales.py data/sales_per_day.txt
"""
from __future__ import print_function

import re
import sys
from operator import add
from pyspark.sql import SparkSession

def perDayProductSales(line):
    """Read line."""
    #print(line)
    parts = re.split(r',', line)
    return parts[2], (int(parts[0]), int(parts[1]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sales <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder\
        .appName("Sales")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])

    #print(lines.collect())
    #lines = lines[1:]
    regions = {}
    result = lines.map(lambda product: perDayProductSales(product)).groupByKey()
    for k, itr in result.collect():
        itrn = spark.sparkContext.parallelize(itr).reduceByKey(add)
        regions[k] = itrn.collect()
    print("Region wise product total sales")
    print(regions)
    spark.stop()
