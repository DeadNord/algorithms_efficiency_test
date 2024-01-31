class GreedyChangeMaker:
    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)

    def find_coins(self, amount):
        result = {}
        for coin in self.denominations:
            if amount >= coin:
                num_coins = amount // coin
                amount -= num_coins * coin
                result[coin] = num_coins
        return result
