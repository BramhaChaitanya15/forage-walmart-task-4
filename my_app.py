import csv

products = []

with open('data/shipping_data_0.csv') as csvfile0:
  csvReader = csv.reader(csvfile0)
  
  for row in csvReader:
    product = row[2]
    if product not in products:
      products.append(product)

print(products)
