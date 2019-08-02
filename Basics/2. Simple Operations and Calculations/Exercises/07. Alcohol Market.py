whiskeyPrice = float(input())

beerQuantity = float(input())
wineQuantity = float(input())
rakiaQuantity = float(input())
whiskeyQuantity = float(input())

rakiaPrice = whiskeyPrice / 2
winePrice = rakiaPrice - (0.4 * rakiaPrice)
beerPrice = rakiaPrice - (0.8 * rakiaPrice)

beerFinalPrice = beerQuantity * beerPrice
wineFinalPrice = wineQuantity * winePrice
rakiaFinalPrice = rakiaQuantity * rakiaPrice
whiskeyFinalPrice = whiskeyQuantity * whiskeyPrice

result = beerFinalPrice + wineFinalPrice + rakiaFinalPrice + whiskeyFinalPrice

print("%.2f" % result)
