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

with open('data/shipping_data_1.csv') as csvfile1:
  csvReader = csv.reader(csvfile1)
  skipped = False
  
  for row in csvReader:
    if not skipped:
      skipped = True
      continue
    product = row[1]
    if product not in products:
      products.append(product)
      
print(products)
