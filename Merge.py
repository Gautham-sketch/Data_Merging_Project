import pandas as pd
import csv

data1 = []
with open("Scraper.csv",'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data1.append(row)
header1 = data1[0]
star_data1 = data1[1: ]

data2 = []
with open("New.csv",'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows("")
    for row in csv_writer:
        data2.append(row)
header2 = data2[0]
star_data2 = data2[1: ]

final_headers = header1 + header2
final_data = []

for index,i in enumerate(star_data1):
    final_data.append(star_data1[index] + star_data2[index])

with open("Final.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(final_headers)
    writer.writerows(final_data)