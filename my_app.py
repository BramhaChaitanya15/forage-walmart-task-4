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
shipmentId = []
shiprows = {}
skip = False
with open('data/shipping_data_2.csv') as csvfile2:
  with open('data/shipping_data_1.csv') as csvfile1:
    csvProductReader1 = csv.reader(csvfile1)
    tide=""
    tanam=""
    taqua=0
    for row in csvProductReader1:
      if not skip:
        skip = True
        continue
      shipID = row[0]
      product = row[1]
      time = row[2]
      if time != "false":
        if tide!=shipID or tanam !=product:
          shiprow={}
          shiprow["shipid"]=tide
          shiprow["product"]=tanam
          shiprow["quantity"]=taqua
          if tide!="" and tanam!="" and taqua!=0:
            shipmentId.append(shiprow)
          tide=shipID
          tanam=product
          taqua=0
        taqua+=1
        shipmentId.append(shipID)
        if product not in products:
          products.append(product)
          
#print(shipmentId)
    csvReader2 = csv.reader(csvfile2)
    for shiprow in shipmentId:
      sid=shiprow["shipid"]
      csvfile2.seek(0)
      for row in csvReader2:
        shipid2 = row[0] 
        if shipid2 == sid:
          shiprow["origin"] = row[1]
          shiprow["destination"] = row[2]
      shipment.append(shiprow)
          
'''
    csvReader2 = csv.reader(csvfile2)
    for row in csvReader2:
      csvfile1.seek(0)
      
      csvReader1 = csv.reader(csvfile1)
'''     
connection = sqlite3.connect("shipment_database.db")

cursor = connection.cursor()
i = 1
for product in products:
  cursor.execute("INSERT INTO product VALUES ( " + str(i) + ", '" + product + "')")
  i+=1
connection.commit()
view = cursor.execute("SELECT * FROM product")
print(view.fetchall())

j = 1
for shiprow in shipment:
  proID = cursor.execute("SELECT id FROM product WHERE name = '" + shiprow["product"] + "'").fetchone()
  cursor.execute("INSERT INTO shipment VALUES ( " + str(j) + "," + str(proID[0]) + ","
                 + str(shiprow["quantity"]) + ", '" + shiprow["origin"] + "','" + shiprow["destination"] + "')")
  j+=1
  
connection.commit()
view = cursor.execute("SELECT * FROM shipment")
print(view.fetchall())
