
import os, requests,json
from sys import argv
apiKey = os.environ['BEST_BUY_API_KEY']

bestBuyParams = {"show": "name,sku,manufacturer,modelNumber,upc,shortDescription,salesRankLongTerm",
                 "format": "json",
                 "apiKey": apiKey}
resp = requests.get("http://api.remix.bestbuy.com/v1/products(search=%s)" % argv[1], params=bestBuyParams)

r = json.loads(resp.text)
for item in r['products']:
    print("%s sells %s" % (item['name'], item['salesRankLongTerm']))
