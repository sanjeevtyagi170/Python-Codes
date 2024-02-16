#run the config fie
# %run /<notebook_path>

#import required functions
import dlt
from pyspark.sql.types import *

#define schema
order_schema = StructType([
    StructField('ORDER_ID',IntegerType(),False),
    StructField('ORDER_DATETIME',StringType(),False),
    StructField('CUSTOMER_ID',IntegerType(),False),
    StructField('ORDER_STATUS',StringType(),False),
    StructField('STORE_ID',IntegerType(),False)
])

#create silver tables
@dlt_table
def orders_silver():
    df = spark.read.option('header',True).schema(order_schema).csv('file_path')
    return df

#Read silver tables and apply required transformation
@dlt_table
@dlt.expect("ORDER_ID_NOT_NULL","ORDER ID IS NOT NULL") # data quality rules
def order_details_gold(table_nm: str):
    orders_silver = dlt.read('orders_silver')
    order_items_silver = dlt.read('order_items_silver')
    order_details = orders_silver.join(order_items_silver,ON = 'ORDER_ID','left')
    order_details = order_details.select(orders_silver['ORDER_ID'],order_silver['ORDER_DATE'],order_silver['CUSTOMER_ID'],order_items_silver['PRODUCT_ID'],order_items_silver['UNIT_PRICE'],order_items_silver['QUANTITY'])
    order_details = order_details.withColumn('SUB_TOTAL_AMOUNT',order_details['UNIT_PRICE']*order_details['QUANTITY'])
    return order_details   
	
	
#Aggregate the data
@dlt_table
def monthly_sales_gold():
    order_details = dlt.read('order_details_gold')

    monthly_sales = order_details.withColumn('MONTH_YEAR',date_format(order_details['ORDER_DATE'],'yyyy-MM'))
    monthly_sales = monthly_sales.groupBy('MONTH_YEAR').sum('SUB_TOTAL_AMOUNT')
    monthly_sales = monthly_sales.withColumn('TOTAL_SALES',round(sum('SUB_TOTAL_AMOUNT'),2).sort('MONTH_YEAR').desc())
    monthly_sales = monthly_sales.select('MONTH_YEAR','TOTAL_SALES')

   return monthly_sales 	
	