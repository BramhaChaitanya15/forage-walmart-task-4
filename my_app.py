import csv

products = []

with open('data/shipping_data_0.csv') as csvfile0:
  csvReader = csv.reader(csvfile0)
  skipped = False
  
  for row in csvReader:
    if not skipped:
      skipped = True
      continue
    product = row[2]
    if product not in products:
      products.append(product)

print(products)
