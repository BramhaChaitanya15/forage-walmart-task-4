import csv
import sqlite3

products = []
shipment = []

with open('data/shipping_data_0.csv') as csvfile0:
  csvReader = csv.reader(csvfile0)
  skipped = False
  
  for row in csvReader:
    if not skipped:
      skipped = True
      continue
   
    origin = row[0]
    destination = row[1]
    product = row[2]
    time = row[3]
    quantity = row[4]
    shiprow = {} 
    if time != "false":
      if product not in products:
        products.append(product)
        
      shiprow["product"] = product
      shiprow["origin"] = origin
      shiprow["destination"] = destination
      shiprow["quantity"] = quantity
      
      shipment.append(shiprow)
      
#print(shipment)

'''with open('data/shipping_data_2.csv') as csvfile2:
  csvReader = csv.reader(csvfile2)
'''

with open('data/shipping_data_1.csv') as csvfile1:
  csvReader = csv.reader(csvfile1)
  for row in csvReader:
    if not skipped:
      skipped = True
      continue
    product = row[1]
    time = row[2]
    if time != "false":
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
'''
j = 1
for shiprow in shipment:
  proID = cursor.execute("SELECT id FROM product WHERE name = '" + shiprow["product"] + "'").fetchone()
  cursor.execute("INSERT INTO shipment VALUES ( " + str(j) + "," + str(proID[0]) + ","
                 + str(shiprow["quantity"]) + ", '" + shiprow["origin"] + "','" + shiprow["destination"] + "')")
  j+=1
  
connection.commit()'''
#view = cursor.execute("SELECT * FROM shipment")
#print(view.fetchall())
