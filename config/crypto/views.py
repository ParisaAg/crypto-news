from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
    price=json.loads(price_request.content)

    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_request.content)


    return render(request,'home.html',{'api' : api,'price':price})


def prices(request):
    if request.method =='POST':
        import requests
        import json
        crypto_request = requests.get("")
        crypto = json.loads(crypto_request.content)
        quote= request.POST['quote']
        return render(request,'prices.html',{'quote':quote})
    else:
        return render(request, 'prices.html', {})
