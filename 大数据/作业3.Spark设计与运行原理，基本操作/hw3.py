from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("My App")
sc=SparkContext(conf=conf)

sc
lines = sc.textFile("file:///home/yokina/my.txt")
lines
words=lines.flatMap(lambda line:line.split())
words
wordKV=words.map(lambda word:(word,1))
wordKV
lineKV=lines.map(lambda line:(1,line))
lineKV
lines.foreach(print)
words.foreach(print)
wordKV.foreach(print)
lineKV.foreach(print)