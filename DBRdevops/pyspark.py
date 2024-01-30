from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, sum
import pandas as pd
import numpy as np
import random

spark = SparkSession.builder.appName("sparkWindowFunctionsExample").getOrCreate()
data = [(1,100,1,2022),(1,700,2,2022),(1,600,2,2022),(2,1000,3,2022),(2,1100,1,2022),(3,400,1,2021),(3,500,1,2021)]
df = spark.createDataFrame(data,schema=["id","salary","month","year"])
df.createOrReplaceTempView("df")
window_1=Window.partitionBy(["year","month"]).orderBy("salary")
df=df.withColumn("ytd_sum",sum("salary").over(window_1)).drop("id")
df.show()

df2=spark.sql("""SELECT
    salary,
    month,
    year,
    SUM(salary) OVER (PARTITION BY year,month ORDER BY salary) AS ytd_sum
FROM df
ORDER BY year, month;""")
df2.show()

df_dict={"id":[1,1,1,2,2,3,3],"salary":[100,700,600,1000,1100,400,500],"month":["1","2","2","3","1","1","1"],
    "year":[2022,2022,2022,2022,2022,2021,2021]}
df=pd.DataFrame(df_dict)
display(df)
df["YTD Sum"]=df[["year","month","salary"]].groupby(["year","month"])["salary"].cumsum()
df.sort_values(["year","month"]).drop("id",axis=1)

######### TESTING FOR SOME BIG DATA #########

def generate_data(num_rows):
    names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Harry", "Isabella", "Jack"]  # Example names
    salaries = range(40000, 120001, 5000)  # Salary range
    data = [(random.choice(names), random.choice(salaries)) for _ in range(num_rows)]
    return data

# Generate 100000 rows of data
list_1 = generate_data(5000000)
print(list_1[0:2])


def find_tuples_above_average(list_1):
   average_salary = sum(i[1] for i in list_1) / len(list_1)
   return [(name, salary) for name, salary in list_1 if salary > average_salary]
high_earners = find_tuples_above_average(list_1)
print(len(high_earners))
