/* In the last exercise, you converted the column plane_year to an integer. This column holds the year each plane was manufactured. However, your model will use the planes' age, which is slightly different from the year it was made! */

# Create the column plane_age
model_data = model_data.withColumn("plane_age", model_data.year-model_data.plane_year)
