def static_tower_data():
  # Placeholder DataFrame (simulates reading from "cell_towers.json.gz")
  df_towers = spark.createDataFrame([
    (12345, "Anytown", "Any County", "Any State", [-74.0060, 40.7128]),
    (67890, "Cityville", "Countyville", "Stateville", [-73.9857, 40.7042]),
    (24680, "Smalltown", "Small County", "Small State", [-73.9960, 40.7270]),
    # ... 17 more rows with placeholder values
  ], ["GlobalID", "City", "County", "State", "coordinates"])

  # Data selection as in the prompt
  return df_towers.select(
      df_towers.GlobalID.alias("GlobalID"),
      df_towers.City.alias("City"),
      df_towers.County.alias("County"),
      df_towers.State.alias("State"),
      df_towers.coordinates[0].alias("Longitude"),
      df_towers.coordinates[1].alias("Latitude")
  ).show(20)  # Show 20 rows using Spark's show() method
  
  static_tower_data()
