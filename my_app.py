import csv
with open('data/shipping_data_0.csv') as csvfile0:
  csvReader = csv.reader(csvfile0)
  for row in csvReader:
    print(row)
