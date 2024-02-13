import pandas as pd
data= {'City Name' : ['Delhi','Mumbai','Bangalore','Hyderabad'],'City Population' : [100,100,200,300]
}
 
df = pd.DataFrame(data)
avg_population = []
total_population = df['City Population'].sum()
num_city=len(df)
 
for index, row in df.iterrows():
    population_exc_city= total_population - row['City Population']
    avg_population.append(population_exc_city/(num_city-1))
 
df['avg_pop'] = avg_population
del df['City Population']
print(df)