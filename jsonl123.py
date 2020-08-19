import jsonlines
'''import json

f=open("stock.txt","r")
a=f.read()
f.close()
#print(a)'''
JSON_file ={"timestamp":1597343948,
    "stocks" : [
         
        {
          "prevClose": 452.04, 
          "bidPrice": 457.1,
          "mid": 460.25,
          "high": 464.14,
          "tngoLast": 458.89,
          "askSize": 100,
          "bidSize": 100,
          "lastSize": 100,
          "lastSaleTimestamp": "2020-08-13T14:38:46.694741176-04:00",
          "ticker": "AAPL",
          "timestamp": "2020-08-13T14:38:46.694741176-04:00",
          "open": 457.79,
          "last": 458.89,
          "volume": 247656,
          "askPrice": 463.4,
          "quoteTimestamp": "2020-08-13T14:38:18.309617924-04:00",
          "low": 455.82
        },
        {
          "prevClose": 452.04, 
          "bidPrice": 457.1,
          "mid": 460.25,
          "high": 464.14,
          "tngoLast": 458.89,
          "askSize": 150,
          "bidSize": 200,  
          "lastSize": 300,
          "lastSaleTimestamp": "2020-08-13T14:38:46.694741176-04:00",
          "ticker": "AAPL",
          "timestamp": "2020-08-13T14:38:46.694741176-04:00",
          "open": 457.89,
          "last": 658.89,
          "volume": 747656,
          "askPrice": 963.4,
          "quoteTimestamp": "2020-08-13T14:38:18.309617924-04:00",
          "low": 955.82 
        }
    ]


    
    
    
}

   


with jsonlines.open('stock.jsonl', 'w') as writer:
    writer.write(JSON_file)
    writer.close()
    

