import csv
import sqlite3

products = []
shipment = []
#accessing data of first csv file
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
      
#accessing data of second and third csv file
shipmentId = []
shiprows = {}
skip = False
with open('data/shipping_data_2.csv') as csvfile2:
  with open('data/shipping_data_1.csv') as csvfile1:
    csvProductReader1 = csv.reader(csvfile1)
    tid=""
    tname=""
    tqua=0
    for row in csvProductReader1:
      if not skip:
        skip = True
        continue
      shipID = row[0]
      product = row[1]
      time = row[2]
      if time != "false":
        if tid!=shipID or tname !=product:
          shiprow={}
          shiprow["shipid"]=tid
          shiprow["product"]=tname
          shiprow["quantity"]=tqua
          if tid!="" and tname!="" and tqua!=0:
            shipmentId.append(shiprow)
          tid=shipID
          tname=product
          tqua=0
        tqua+=1
        
        if product not in products:
          products.append(product)
          
    shiprow={}
    shiprow["shipid"]=tid
    shiprow["product"]=tname
    shiprow["quantity"]=tqua
    shipmentId.append(shiprow)
    

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
 
#for inserting data in the database
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
