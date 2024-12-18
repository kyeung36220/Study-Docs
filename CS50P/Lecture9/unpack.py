def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100,50,25]

print(total(*coins), "Knuts") # *coins unpacks coins fast and easy and for dictionary is two stars **coins
