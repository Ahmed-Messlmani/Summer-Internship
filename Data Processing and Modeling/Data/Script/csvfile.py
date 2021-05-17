import csv
import csv
f=open('D://NLP project//dataset//final//new//finalsentence.txt','r',encoding='latin-1')
lines = f.readlines()
f.close()
f1=open('D://NLP project//dataset//final//new//cleantitle2.txt','r',encoding='latin-1')
lines1 = f1.readlines()
f1.close()
with open('D://NLP project//dataset//final//cleandata2.csv', 'a',encoding='latin-1', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["title","label"])
    for line in lines:
    	writer.writerow([line, "1"])
    for line in lines1:
    	writer.writerow([line, "0"])


    