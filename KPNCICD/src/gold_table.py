#Run the config file
# %run ../<path to config file>

#Import functions
from pyspark.sql.functions import *

# Read data from silver layer
silver_df = spark.read.format("delta").load("<file_path>")

#Join with other tables(optional)
joined_df = silver_df.join(df2,on = "column1",how = "inner").select(silver_df.column1,df2.column2, ...)

# Apply transformations and aggregations
gold_df = joined_df.groupBy("id", "column1").agg(sum("column2").alias("column2"))

# Write table to gold layer
gold_df.write.format("delta").mode("overwrite").saveAsTable("catalog.schema.your_gold_table_name")