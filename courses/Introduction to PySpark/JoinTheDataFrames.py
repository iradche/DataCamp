/* In the next two chapters you'll be working to build a model that predicts whether or not a flight will be delayed based on the flights data we've been working with. This model will also include information about the plane that flew the route, so the first step is to join the two tables: flights and planes! */

# Rename year column
planes = planes.withColumnRenamed('year', 'plane_year')

# Join the DataFrames
model_data = flights.join(planes, on='tailnum', how="leftouter")
