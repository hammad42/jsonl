import jsonlines
import json

f=open("stock.json","r")
a=f.read()
f.close() #convert string into json or string into dictionary
#print(a)
b=json.loads(a) #here we convert string into dictionary
print(type(b))


   


with jsonlines.open('stock.jsonl', 'w') as writer:
    writer.write(b)
    writer.close()
    

