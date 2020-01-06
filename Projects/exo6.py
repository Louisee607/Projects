import urllib.request
import csv
import requests 

mylist = []
link = "https://download.bls.gov/pub/time.series/ap/ap.data.0.Current"
myfile = requests.get(link)
#print(myfile)
with open('data.csv', 'wb') as f:
    f.write(myfile.content)
    f.close()


file = open('data.csv')
csv_f = csv.reader(file)

for row in csv_f:
  mylist.append(row)

print(mylist)

