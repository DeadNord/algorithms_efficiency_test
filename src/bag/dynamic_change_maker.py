class DynamicChangeMaker:
    def __init__(self, denominations):
        self.denominations = sorted(denominations)

    def find_coins(self, amount):
        min_coins = [float("inf")] * (amount + 1)
        min_coins[0] = 0

        last_coin = [0] * (amount + 1)

        for coin in self.denominations:
            for i in range(coin, amount + 1):
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    last_coin[i] = coin

        result = {}
        while amount > 0:
            coin = last_coin[amount]
            result[coin] = result.get(coin, 0) + 1
            amount -= coin

        return result
