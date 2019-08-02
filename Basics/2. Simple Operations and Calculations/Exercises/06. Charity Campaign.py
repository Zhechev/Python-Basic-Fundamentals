campaignDays = int(input())
bakersNum = int(input())
cakesNum = int(input())
wafflesNum = int(input())
pancakesNum = int(input())

bakerCakesPerDay = cakesNum * 45
bakerWafflesPerDay = wafflesNum * 5.80
bakerPancakesPerDay = pancakesNum * 3.20

finalMoneyPerDayOneBaker = bakerCakesPerDay + bakerWafflesPerDay + bakerPancakesPerDay
finalMoneyAllBakersPerDay = finalMoneyPerDayOneBaker * bakersNum
finalMoneyAllBakers = finalMoneyAllBakersPerDay * campaignDays
oneEightPart = finalMoneyAllBakers / 8
result = finalMoneyAllBakers - oneEightPart
print("%.2f" % result)
