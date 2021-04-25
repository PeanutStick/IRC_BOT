from urllib.request import Request, urlopen
import re

def main(ticket):
    market="https://coinmarketcap.com/en/currencies/"+str(ticket)+"/"
    req = Request(market, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    price = re.search(r'class="priceValue(.*)</div>', str(webpage))
    price = re.search(r'">(.*)</div', str(price)).group(1)
    pourcentage = re.search(r'class="icon-Caret(.*)<!-- -->%', str(webpage))
    if "down" in str(pourcentage):
        state = "-"
    else:
        state = "+"
    pourcentage = str(pourcentage).split("></span>")[1]
    pourcentage = str(pourcentage).split("<!--")[0]
    out = price+" "+state+pourcentage+"%"
    return out
if __name__ == "__main__":
    print(main(buff))
