from pyspark import SparkContext, SparkConf
import sys

conf = SparkConf().setAppName("myTestApp")
sc = SparkContext(conf=conf)

log4jLogger = sc._jvm.org.apache.log4j
log = log4jLogger.LogManager.getLogger(__name__)
log.warn("Python version is:")
log.warn(sys.version)

#words = sc.textFile("/data/test.txt")
#words.saveAsTextFile("/data/test2.txt")
