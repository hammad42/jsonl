import jsonlines
import json
import requests
headers = {
    'Content-Type': 'application/json'
}

requestResponse = requests.get("https://api.tiingo.com/iex/?tickers=aapl,spy&token=7d1986e9b07d97f737a1645459a8453acfacac35", headers=headers)

#print(type(requestResponse.json()))
#print(requestResponse.json())
a=str(requestResponse.json())
#print("#####################")
#print(a)

'''
f=open("stock.json","r")
a=f.read()
f.close() #convert string into json or string into dictionary
#'''
#b=json.loads(a) #here we convert string into dictionary
#print(a)


   


with jsonlines.open('stock.jsonl', 'w') as writer:


    writer.write(a)


    writer.close()
f=open('stock.jsonl')
k=f.read()
print(k)
     

