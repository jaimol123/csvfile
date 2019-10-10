import json
import csv


f2=open("data.json")
jsondata=json.load(f2)
#print(jsondata)

for x in jsondata:
	x["name"]=x["first_name"]+" "+x["last_name"]
	

	if "first_name" in x:
		x.pop("first_name")
		

	if "last_name" in x:
		x.pop("last_name")
	#print(x)


lis2=[]
lis=[]
lis1=[]
lis3=[]
f1=open("table.csv","w")
csvwriter=csv.writer(f1)
for i in jsondata:
	y=i.keys()
	lis=list(y)
		

for i in range(0,len(lis)):
	q=(lis[i]).capitalize()
	lis1.append((q))
	
lis2=list('\033[1m'+str(lis1))
print(lis2)

csvwriter.writerow(lis1)

for i in jsondata:
	csvwriter.writerow(i.values()) 		

