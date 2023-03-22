import csv
import sqlite3

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
      
connection = sqlite3.connect("shipment_database.db")

cursor = connection.cursor()
i = 1
for product in products:
  cursor.execute("INSERT INTO product VALUES ( " + str(i) + ", '" + product + "')")
  i+=1
connection.commit()
view = cursor.execute("SELECT * FROM product")
print(view.fetchall())
