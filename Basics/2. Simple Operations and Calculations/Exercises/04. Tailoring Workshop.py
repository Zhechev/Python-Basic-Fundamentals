rectangleTables = int(input())
rectangleTablesLength = float(input())
rectangleTablesWidth = float(input())

areaTables = rectangleTables * (rectangleTablesLength + 2 * 0.30) * (rectangleTablesWidth + 2 * 0.30)
areaCares = rectangleTables * (rectangleTablesLength / 2) * (rectangleTablesLength / 2)

priceDollars = (areaTables * 7) + (areaCares * 9)
priceLevas = priceDollars * 1.85

print("%.2f" % priceDollars + ' USD')
print("%.2f" % priceLevas + ' BGN')
