content=open('D://NLP project//dataset//bad word.txt',encoding="latin-1").readlines()

content_set=set(content)

cleandata=open('D://NLP project//dataset//final//new//testword.txt', 'w',encoding='latin-1')

for line in content_set:
	cleandata.write(line)




	