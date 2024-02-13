df ['Start']=pd.to_datetime(df ['Start']) 
df ['End']=pd.to_datetime(df ['End']) 
df['diff']=(df ['End'] - df ['Start']).dt.total_seconds()/60
print(df)