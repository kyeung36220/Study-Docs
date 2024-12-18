


def main():
    price = 50
    while price > 0:
        coin = get_coin(price)
        price -= coin
    print("Change Owed:", abs(price))

def get_coin(x):
    while True:
        print("Amount Due:", x)
        coin_inserted = int(input("Insert Coin: "))
        if coin_inserted == 25 or coin_inserted == 10 or coin_inserted == 5:
            return coin_inserted

main()
